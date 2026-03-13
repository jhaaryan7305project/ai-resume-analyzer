import google.generativeai as genai
from PyPDF2 import PdfReader
import docx
from datetime import datetime, date
import re, os, secrets
import psycopg2
import psycopg2.errors
import psycopg2.extras
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from flask import send_file, jsonify, redirect, url_for, flash
import io
from flask import Flask, render_template, request, session
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeTimedSerializer

from job_database import (
    get_job_info, get_available_roles, get_available_companies
)

# ─────────────────────────────────────────────────────────────────────────────
# APP CONFIG
# ─────────────────────────────────────────────────────────────────────────────
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "fallback_for_local")

# ── Gmail SMTP (works from localhost as long as you have internet) ─────────────
app.config["MAIL_SERVER"]         = "smtp.gmail.com"
app.config["MAIL_PORT"]           = 587
app.config["MAIL_USE_TLS"]        = True
app.config["MAIL_USE_SSL"]        = False
app.config["MAIL_USERNAME"]       = "jhaaryan7305@gmail.com"
app.config["MAIL_PASSWORD"]       = os.environ.get("MAIL_APP_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = ("AI Resume Analyzer", "jhaaryan7305@gmail.com")

ADMIN_EMAIL    = "jhaaryan7305@gmail.com"
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")
DAILY_LIMIT    = 3

mail       = Mail(app)
login_mgr  = LoginManager(app)
login_mgr.login_view = "login_page"
serializer = URLSafeTimedSerializer(app.secret_key)

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel(
    "models/gemini-flash-latest",
    generation_config={"temperature": 0, "top_p": 1, "top_k": 1}
)

# ─────────────────────────────────────────────────────────────────────────────
# DATABASE  (PostgreSQL)
# ─────────────────────────────────────────────────────────────────────────────
DATABASE_URL = os.environ.get("DATABASE_URL")

def get_db():
    conn = psycopg2.connect(DATABASE_URL, cursor_factory=psycopg2.extras.RealDictCursor)
    return conn

def init_db():
    conn = get_db()
    c    = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users (
        id            SERIAL PRIMARY KEY,
        email         TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        is_admin      INTEGER DEFAULT 0,
        created_at    TEXT DEFAULT to_char(now(),'YYYY-MM-DD HH24:MI:SS'),
        daily_count   INTEGER DEFAULT 0,
        last_date     TEXT DEFAULT ''
    )""")
    c.execute("""CREATE TABLE IF NOT EXISTS history (
        id                 SERIAL PRIMARY KEY,
        user_id            INTEGER NOT NULL,
        filename           TEXT,
        company            TEXT,
        job_role           TEXT,
        score              INTEGER,
        strengths          TEXT,
        improvements       TEXT,
        feedback           TEXT,
        must_found         TEXT,
        must_missing       TEXT,
        good_found         TEXT,
        good_missing       TEXT,
        must_match_percent INTEGER,
        match_percent      INTEGER,
        job_description    TEXT,
        created_at         TEXT DEFAULT to_char(now(),'YYYY-MM-DD HH24:MI:SS'),
        FOREIGN KEY (user_id) REFERENCES users(id)
    )""")
    conn.commit()
    c.execute("SELECT id FROM users WHERE email=%s", (ADMIN_EMAIL,))
    existing = c.fetchone()
    if not existing:
        c.execute("INSERT INTO users (email,password_hash,is_admin) VALUES (%s,%s,1)",
                  (ADMIN_EMAIL, generate_password_hash(ADMIN_PASSWORD)))
        conn.commit()
    conn.close()

init_db()

# ─────────────────────────────────────────────────────────────────────────────
# USER MODEL
# ─────────────────────────────────────────────────────────────────────────────
class User(UserMixin):
    def __init__(self, row):
        self.id          = row["id"]
        self.email       = row["email"]
        self.is_admin    = bool(row["is_admin"])
        self.daily_count = row["daily_count"]
        self.last_date   = row["last_date"]

@login_mgr.user_loader
def load_user(user_id):
    conn = get_db()
    c    = conn.cursor()
    c.execute("SELECT * FROM users WHERE id=%s", (user_id,))
    row  = c.fetchone()
    conn.close()
    return User(row) if row else None

# ─────────────────────────────────────────────────────────────────────────────
# DAILY LIMIT
# ─────────────────────────────────────────────────────────────────────────────
def get_today_count(user_id):
    today = str(date.today())
    conn  = get_db()
    c     = conn.cursor()
    c.execute("SELECT daily_count, last_date FROM users WHERE id=%s", (user_id,))
    row   = c.fetchone()
    conn.close()
    return 0 if row["last_date"] != today else row["daily_count"]

def increment_count(user_id):
    today = str(date.today())
    conn  = get_db()
    c     = conn.cursor()
    c.execute("SELECT last_date FROM users WHERE id=%s", (user_id,))
    row   = c.fetchone()
    if row["last_date"] != today:
        c.execute("UPDATE users SET daily_count=1, last_date=%s WHERE id=%s", (today, user_id))
    else:
        c.execute("UPDATE users SET daily_count=daily_count+1 WHERE id=%s", (user_id,))
    conn.commit()
    conn.close()

# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────
def extract_text(file):
    if file.filename.endswith(".pdf"):
        reader = PdfReader(file)
        return "".join(page.extract_text() or "" for page in reader.pages)
    elif file.filename.endswith(".docx"):
        doc = docx.Document(file)
        return "\n".join(p.text for p in doc.paragraphs)
    return None

def keyword_match(resume_text, keywords):
    resume_lower = resume_text.lower()
    found, missing = [], []
    for kw in keywords:
        (found if kw.lower() in resume_lower else missing).append(kw)
    total = len(keywords)
    return int(len(found)/total*100) if total else 0, found, missing

def build_gap_analysis(must_have, good_to_have, must_found, must_missing, found_kw, missing_kw):
    rows = []
    for s in must_have:
        f = s in must_found
        rows.append({"skill":s,"priority":"Must-Have","found":f,
                     "action":"Keep it highlighted" if f else "Add to resume ASAP — deal-breaker"})
    for s in good_to_have:
        f = s in found_kw
        rows.append({"skill":s,"priority":"Good-to-Have","found":f,
                     "action":"Good bonus skill" if f else "Consider adding for higher score"})
    return rows

def base_ctx():
    used = get_today_count(current_user.id) if current_user.is_authenticated else 0
    return dict(
        score=None, strengths=[], improvements=[], feedback="",
        match_percent=0, found_keywords=[], missing_keywords=[],
        must_have_keywords=[], good_to_have_keywords=[],
        must_found=[], must_missing=[], good_found=[], good_missing=[],
        must_match_percent=0, gap_analysis=[],
        company=None, job_role=None, job_description="",
        available_companies=get_available_companies(),
        daily_used=used, daily_limit=DAILY_LIMIT,
        history=[]
    )

def get_user_history(user_id):
    conn = get_db()
    c    = conn.cursor()
    c.execute("SELECT * FROM history WHERE user_id=%s ORDER BY created_at DESC LIMIT 30", (user_id,))
    rows = c.fetchall()
    conn.close()
    return [dict(r) for r in rows]

def save_history(user_id, filename, company, job_role, score,
                 strengths, improvements, feedback,
                 must_found, must_missing, good_found, good_missing,
                 must_match_percent, match_percent, job_description):
    conn = get_db()
    c    = conn.cursor()
    c.execute("""INSERT INTO history
        (user_id,filename,company,job_role,score,strengths,improvements,feedback,
         must_found,must_missing,good_found,good_missing,
         must_match_percent,match_percent,job_description)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
        (user_id,filename,company,job_role,score,
         strengths,improvements,feedback,
         must_found,must_missing,good_found,good_missing,
         must_match_percent,match_percent,job_description))
    conn.commit()
    conn.close()

# ─────────────────────────────────────────────────────────────────────────────
# AUTH ROUTES
# ─────────────────────────────────────────────────────────────────────────────
@app.route("/login", methods=["GET","POST"])
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    error = None
    if request.method == "POST":
        email    = request.form.get("email","").strip().lower()
        password = request.form.get("password","")
        conn = get_db()
        c    = conn.cursor()
        c.execute("SELECT * FROM users WHERE email=%s", (email,))
        row  = c.fetchone()
        conn.close()
        if row and check_password_hash(row["password_hash"], password):
            login_user(User(row), remember=True)
            return redirect(url_for("home"))
        error = "Invalid email or password."
    return render_template("login.html", page="login", error=error)

@app.route("/register", methods=["GET","POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    error = None
    if request.method == "POST":
        email    = request.form.get("email","").strip().lower()
        password = request.form.get("password","")
        confirm  = request.form.get("confirm","")
        if not email or not password:
            error = "Email and password are required."
        elif password != confirm:
            error = "Passwords do not match."
        elif len(password) < 6:
            error = "Password must be at least 6 characters."
        else:
            try:
                conn = get_db()
                c    = conn.cursor()
                c.execute("INSERT INTO users (email,password_hash) VALUES (%s,%s)",
                             (email, generate_password_hash(password)))
                conn.commit()
                c.execute("SELECT * FROM users WHERE email=%s", (email,))
                row  = c.fetchone()
                conn.close()
                login_user(User(row), remember=True)
                return redirect(url_for("home"))
            except psycopg2.errors.UniqueViolation:
                error = "An account with this email already exists."
    return render_template("login.html", page="register", error=error)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login_page"))

@app.route("/forgot-password", methods=["GET","POST"])
def forgot_password():
    message = error = None
    if request.method == "POST":
        email = request.form.get("email","").strip().lower()
        conn  = get_db()
        c     = conn.cursor()
        c.execute("SELECT * FROM users WHERE email=%s", (email,))
        user  = c.fetchone()
        conn.close()
        if user:
            token     = serializer.dumps(email, salt="pw-reset")
            reset_url = url_for("reset_password", token=token, _external=True)
            try:
                msg = Message(
                    subject="Reset Your AI Resume Analyzer Password",
                    recipients=[email],
                    html=f"""
                    <div style="font-family:Arial;max-width:480px;margin:auto;padding:30px;
                                border:1px solid #eee;border-radius:10px;">
                      <h2 style="color:#2f3542;">🔐 AI Resume Analyzer</h2>
                      <p>You requested a password reset. Click the button below to set a new password.</p>
                      <a href="{reset_url}"
                         style="display:inline-block;background:#4CAF50;color:white;
                                padding:12px 28px;border-radius:6px;text-decoration:none;
                                font-weight:bold;margin:12px 0;">
                        Reset My Password
                      </a>
                      <p style="color:#888;font-size:12px;margin-top:20px;">
                        ⏱ This link expires in 30 minutes.<br>
                        If you didn't request this, just ignore this email.
                      </p>
                    </div>"""
                )
                mail.send(msg)
                message = "✅ Password reset link sent! Check your inbox."
            except Exception as e:
                error = f"Could not send email: {str(e)}"
        else:
            message = "If that email is registered, a reset link has been sent."
    return render_template("login.html", page="forgot", message=message, error=error)

@app.route("/reset-password/<token>", methods=["GET","POST"])
def reset_password(token):
    try:
        email = serializer.loads(token, salt="pw-reset", max_age=1800)
    except:
        return render_template("login.html", page="login",
                               error="Reset link is invalid or expired. Please request a new one.")
    error = None
    if request.method == "POST":
        password = request.form.get("password","")
        confirm  = request.form.get("confirm","")
        if password != confirm:
            error = "Passwords do not match."
        elif len(password) < 6:
            error = "Password must be at least 6 characters."
        else:
            conn = get_db()
            c    = conn.cursor()
            c.execute("UPDATE users SET password_hash=%s WHERE email=%s",
                         (generate_password_hash(password), email))
            conn.commit()
            conn.close()
            return render_template("login.html", page="login",
                                   message="✅ Password reset! Please log in.")
    return render_template("login.html", page="reset", token=token, error=error)

# ─────────────────────────────────────────────────────────────────────────────
# MAIN ROUTES
# ─────────────────────────────────────────────────────────────────────────────
@app.route("/")
@login_required
def home():
    ctx = base_ctx()
    ctx["history"] = get_user_history(current_user.id)
    return render_template("index.html", **ctx)

@app.route("/get_roles/<company>")
@login_required
def get_roles(company):
    return jsonify(get_available_roles(company))

@app.route("/analyze", methods=["POST"])
@login_required
def analyze():
    # Daily limit
    if not current_user.is_admin:
        used = get_today_count(current_user.id)
        if used >= DAILY_LIMIT:
            ctx = base_ctx()
            ctx["history"] = get_user_history(current_user.id)
            ctx["error"]   = f"⛔ Daily limit reached! You can analyze {DAILY_LIMIT} resumes per day. Come back tomorrow."
            ctx["daily_used"] = used
            return render_template("index.html", **ctx)

    company  = request.form.get("company","").strip()
    job_role = request.form.get("job_role","").strip()
    if request.form.get("custom_company","").strip():  company  = request.form.get("custom_company").strip()
    if request.form.get("custom_job_role","").strip(): job_role = request.form.get("custom_job_role").strip()

    from job_database import get_job_info
    job_info        = get_job_info(company, job_role)
    must_have       = job_info.get("must_have",    [])
    good_to_have    = job_info.get("good_to_have", [])
    job_description = job_info.get("description",  "")

    file = request.files.get("resume")
    if not file:
        ctx = base_ctx(); ctx["error"] = "Please upload your resume file."
        ctx["history"] = get_user_history(current_user.id)
        return render_template("index.html", **ctx)

    text = extract_text(file)
    if not text:
        ctx = base_ctx(); ctx["error"] = "Could not read text from your resume."
        ctx["history"] = get_user_history(current_user.id)
        return render_template("index.html", **ctx)

    all_kw = must_have + good_to_have
    match_percent,      found_kw,   missing_kw  = keyword_match(text, all_kw)
    must_match_percent, must_found, must_missing = keyword_match(text, must_have)
    _,                  good_found, good_missing = keyword_match(text, good_to_have)
    gap_analysis = build_gap_analysis(must_have, good_to_have, must_found, must_missing, found_kw, missing_kw)

    prompt = f"""
You are a senior technical recruiter at {company} screening resumes for {job_role}.

OFFICIAL JOB REQUIREMENTS ({company} database):
Role Description: {job_description}
MUST-HAVE SKILLS (50% of score): {", ".join(must_have)}
GOOD-TO-HAVE SKILLS (25% of score): {", ".join(good_to_have)}

GAP ANALYSIS:
- Must-have FOUND   : {", ".join(must_found)   if must_found   else "None"}
- Must-have MISSING : {", ".join(must_missing) if must_missing else "None"}
- Must-have match   : {must_match_percent}%
- Overall match     : {match_percent}%

Evaluate strictly as a {company} recruiter. Reference specific skills by name in feedback.
Scoring: 50% must-have, 25% experience depth, 25% resume quality.
Rules: Score integer 0-100. No markdown ** or *. Wrap titles in <b>...</b>.

SCORE: <number>

STRENGTHS:
- <b>Title:</b> description
- <b>Title:</b> description
- <b>Title:</b> description

IMPROVEMENTS:
- <b>Title:</b> description naming specific missing skills
- <b>Title:</b> description
- <b>Title:</b> description

OVERALL FEEDBACK:
2-3 lines of specific actionable advice for getting hired as {job_role} at {company}.

Resume:
{text}
"""
    from google.api_core.exceptions import ResourceExhausted
    try:
        result = model.generate_content(prompt).text
    except ResourceExhausted:
        ctx = base_ctx(); ctx["error"] = "⚠️ AI quota exceeded. Try again tomorrow."
        ctx["history"] = get_user_history(current_user.id)
        return render_template("index.html", **ctx)

    sm = re.search(r'SCORE:\s*(\d{1,3})', result)
    score = max(0, min(int(sm.group(1)), 100)) if sm else None

    def sect(txt, s, e=None):
        try:
            p = rf"{s}:\s*(.*?){e}:" if e else rf"{s}:\s*(.*)"
            m = re.search(p, txt, re.S|re.I)
            if not m: return []
            return [l.strip() for l in m.group(1).strip().split("\n") if l.strip().startswith("-")]
        except: return []

    strengths_list    = sect(result, "STRENGTHS",    "IMPROVEMENTS")
    improvements_list = sect(result, "IMPROVEMENTS", "OVERALL FEEDBACK")
    fb = re.search(r'OVERALL FEEDBACK:\s*(.*)', result, re.S|re.I)
    feedback = fb.group(1).strip() if fb else "No feedback generated."

    increment_count(current_user.id)
    save_history(
        current_user.id, file.filename, company, job_role, score,
        "\n".join(strengths_list), "\n".join(improvements_list), feedback,
        ",".join(must_found), ",".join(must_missing),
        ",".join(good_found), ",".join(good_missing),
        must_match_percent, match_percent, job_description
    )

    return render_template("index.html",
        score=score, strengths=strengths_list, improvements=improvements_list,
        feedback=feedback, history=get_user_history(current_user.id),
        company=company, job_role=job_role, job_description=job_description,
        match_percent=match_percent, found_keywords=found_kw, missing_keywords=missing_kw,
        must_have_keywords=must_have, good_to_have_keywords=good_to_have,
        must_found=must_found, must_missing=must_missing,
        good_found=good_found, good_missing=good_missing,
        must_match_percent=must_match_percent, gap_analysis=gap_analysis,
        available_companies=get_available_companies(),
        daily_used=get_today_count(current_user.id), daily_limit=DAILY_LIMIT
    )

# ─────────────────────────────────────────────────────────────────────────────
# PDF ROUTES
# ─────────────────────────────────────────────────────────────────────────────
@app.route("/download_pdf", methods=["POST"])
@login_required
def download_pdf():
    return _build_pdf(
        score=request.form.get("score","N/A"),
        company=request.form.get("company",""),
        job_role=request.form.get("job_role",""),
        strengths_raw=request.form.get("strengths",""),
        improvements_raw=request.form.get("improvements",""),
        feedback_raw=request.form.get("feedback",""),
        job_description=request.form.get("job_description",""),
        must_match=request.form.get("must_match_percent","0"),
        match_pct=request.form.get("match_percent","0"),
        must_found_list  =[s.strip() for s in request.form.get("must_found","").split(",")   if s.strip()],
        must_missing_list=[s.strip() for s in request.form.get("must_missing","").split(",") if s.strip()],
        good_found_list  =[s.strip() for s in request.form.get("good_found","").split(",")   if s.strip()],
        good_missing_list=[s.strip() for s in request.form.get("good_missing","").split(",") if s.strip()]
    )

@app.route("/download_history_pdf/<int:hid>")
@login_required
def download_history_pdf(hid):
    conn = get_db()
    c    = conn.cursor()
    c.execute("SELECT * FROM history WHERE id=%s AND user_id=%s", (hid, current_user.id))
    row  = c.fetchone()
    conn.close()
    if not row: return "Not found", 404
    r = dict(row)
    return _build_pdf(
        score=r["score"], company=r["company"], job_role=r["job_role"],
        strengths_raw=r["strengths"], improvements_raw=r["improvements"],
        feedback_raw=r["feedback"], job_description=r["job_description"] or "",
        must_match=r["must_match_percent"], match_pct=r["match_percent"],
        must_found_list  =r["must_found"].split(",")   if r["must_found"]   else [],
        must_missing_list=r["must_missing"].split(",") if r["must_missing"] else [],
        good_found_list  =r["good_found"].split(",")   if r["good_found"]   else [],
        good_missing_list=r["good_missing"].split(",") if r["good_missing"] else []
    )

def _build_pdf(score, company, job_role, strengths_raw, improvements_raw,
               feedback_raw, job_description, must_match, match_pct,
               must_found_list, must_missing_list, good_found_list, good_missing_list):
    def clean(t): return re.sub(r"<.*?>","", t or "").strip()
    GREEN=colors.HexColor("#27ae60"); RED=colors.HexColor("#e74c3c")
    ORANGE=colors.HexColor("#f39c12"); DARK=colors.HexColor("#2f3542")
    LIGHT=colors.HexColor("#f4f6f8"); BLUE=colors.HexColor("#2980b9")
    WHITE=colors.white

    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf,pagesize=A4,rightMargin=18*mm,leftMargin=18*mm,topMargin=18*mm,bottomMargin=18*mm)
    sty = getSampleStyleSheet()
    n = sty["BodyText"]; n.fontSize=9; n.leading=13
    sm  = ParagraphStyle("sm", parent=n, fontSize=8,  textColor=colors.grey)
    h1  = ParagraphStyle("h1", parent=sty["Heading1"], fontSize=16, textColor=DARK, spaceAfter=4)
    h2  = ParagraphStyle("h2", parent=sty["Heading2"], fontSize=12, textColor=DARK, spaceBefore=10, spaceAfter=4)
    el  = []

    el.append(Paragraph("AI Resume Analyzer — Full Report", h1))
    el.append(HRFlowable(width="100%",thickness=1.5,color=DARK)); el.append(Spacer(1,8))
    try: si=int(score)
    except: si=0
    sc=GREEN if si>=70 else(ORANGE if si>=40 else RED)
    t=Table([["Company",company or "—"],["Job Role",job_role or "—"],
              ["ATS Score",f"{score}%"],["Must-Have Match",f"{must_match}%"],
              ["Overall Match",f"{match_pct}%"]],colWidths=[140,330])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(0,-1),DARK),('TEXTCOLOR',(0,0),(0,-1),WHITE),
        ('FONTNAME',(0,0),(0,-1),'Helvetica-Bold'),('FONTSIZE',(0,0),(-1,-1),9),
        ('BACKGROUND',(1,2),(1,2),sc),('TEXTCOLOR',(1,2),(1,2),WHITE),
        ('FONTNAME',(1,2),(1,2),'Helvetica-Bold'),
        ('ROWBACKGROUNDS',(1,0),(1,-1),[WHITE,LIGHT]),
        ('GRID',(0,0),(-1,-1),0.4,colors.grey),('PADDING',(0,0),(-1,-1),7)]))
    el.append(t); el.append(Spacer(1,10))

    if job_description:
        el.append(Paragraph("About This Role",h2))
        el.append(Paragraph(f"<i>Source: {company} careers page &amp; LinkedIn database</i>",sm))
        el.append(Spacer(1,3)); el.append(Paragraph(clean(job_description),n)); el.append(Spacer(1,8))

    el.append(Paragraph("Gap Analysis — Resume vs Job Database",h2))
    el.append(Paragraph(f"Every skill sourced from {company} database for {job_role}.",n))
    el.append(Spacer(1,6))
    gr=[["Skill","Priority","Status","Action Required"]]
    for s in must_found_list:   gr.append([s,"Must-Have",   "FOUND",   "Keep highlighted"])
    for s in must_missing_list: gr.append([s,"Must-Have",   "MISSING", "Add immediately — critical gap"])
    for s in good_found_list:   gr.append([s,"Good-to-Have","FOUND",   "Good bonus skill"])
    for s in good_missing_list: gr.append([s,"Good-to-Have","MISSING", "Consider adding"])
    if len(gr)>1:
        gt=Table(gr,colWidths=[115,85,65,205],repeatRows=1)
        gs=TableStyle([
            ('BACKGROUND',(0,0),(-1,0),DARK),('TEXTCOLOR',(0,0),(-1,0),WHITE),
            ('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),('FONTSIZE',(0,0),(-1,-1),8.5),
            ('GRID',(0,0),(-1,-1),0.4,colors.grey),('PADDING',(0,0),(-1,-1),6),
            ('ROWBACKGROUNDS',(0,1),(-1,-1),[WHITE,LIGHT]),('VALIGN',(0,0),(-1,-1),'MIDDLE')])
        for i,row in enumerate(gr[1:],1):
            if row[2]=="MISSING" and row[1]=="Must-Have":
                gs.add('TEXTCOLOR',(2,i),(2,i),RED);gs.add('FONTNAME',(2,i),(2,i),'Helvetica-Bold')
                gs.add('TEXTCOLOR',(3,i),(3,i),RED);gs.add('FONTNAME',(3,i),(3,i),'Helvetica-Bold')
            elif row[2]=="FOUND": gs.add('TEXTCOLOR',(2,i),(2,i),GREEN);gs.add('FONTNAME',(2,i),(2,i),'Helvetica-Bold')
            elif row[2]=="MISSING": gs.add('TEXTCOLOR',(2,i),(2,i),ORANGE)
        gt.setStyle(gs); el.append(gt)
    else: el.append(Paragraph("No gap data.",n))
    el.append(Spacer(1,12))

    for title,raw,lc in [("Strengths",strengths_raw,GREEN),("Improvements Needed",improvements_raw,RED)]:
        el.append(Paragraph(title,h2)); el.append(HRFlowable(width="100%",thickness=0.5,color=lc)); el.append(Spacer(1,4))
        for line in clean(raw).split("\n"):
            line=line.strip().lstrip("-").strip()
            if line: el.append(Paragraph(f"• {line}",n))
        el.append(Spacer(1,10))

    el.append(Paragraph("Overall Feedback",h2))
    el.append(HRFlowable(width="100%",thickness=0.5,color=BLUE)); el.append(Spacer(1,4))
    el.append(Paragraph(clean(feedback_raw),ParagraphStyle("fb",parent=n,backColor=colors.HexColor("#eaf4fb"),borderPad=8)))
    el.append(Spacer(1,14))
    el.append(HRFlowable(width="100%",thickness=0.5,color=colors.lightgrey)); el.append(Spacer(1,4))
    el.append(Paragraph(f"AI Resume Analyzer  |  {datetime.now().strftime('%d %b %Y %H:%M')}  |  Skills from {company} careers page &amp; LinkedIn.",sm))

    doc.build(el); buf.seek(0)
    fname=f"resume_report_{company}_{job_role}.pdf".replace(" ","_")
    return send_file(buf,as_attachment=True,download_name=fname,mimetype="application/pdf")

# ─────────────────────────────────────────────────────────────────────────────
# ADMIN PANEL
# ─────────────────────────────────────────────────────────────────────────────
@app.route("/admin")
@login_required
def admin_panel():
    if not current_user.is_admin:
        return "Access denied.", 403
    conn = get_db()
    c    = conn.cursor()
    c.execute("SELECT * FROM users ORDER BY created_at DESC")
    users = c.fetchall()
    c.execute("SELECT h.*,u.email FROM history h JOIN users u ON h.user_id=u.id ORDER BY h.created_at DESC LIMIT 100")
    all_history = c.fetchall()
    conn.close()
    return render_template("admin.html",
        users=[dict(u) for u in users],
        all_history=[dict(h) for h in all_history])

@app.route("/admin/delete_user/<int:uid>", methods=["POST"])
@login_required
def delete_user(uid):
    if not current_user.is_admin: return "Access denied.", 403
    conn = get_db()
    c    = conn.cursor()
    c.execute("DELETE FROM history WHERE user_id=%s", (uid,))
    c.execute("DELETE FROM users WHERE id=%s AND is_admin=0", (uid,))
    conn.commit(); conn.close()
    return redirect(url_for("admin_panel"))

if __name__ == "__main__":
    app.run(debug=True)