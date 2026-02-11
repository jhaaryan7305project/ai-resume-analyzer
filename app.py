import google.generativeai as genai
from PyPDF2 import PdfReader
import docx
from datetime import datetime
import re
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from flask import send_file
import io
from flask import Flask, render_template, request, send_file, session

app = Flask(__name__)
app.secret_key = "resume_analyzer_secret_123"

genai.configure(api_key="AIzaSyD9Src8JJqZ_D5X0XHl5oluN23KVjiDk6Q")

model = genai.GenerativeModel(
    "models/gemini-flash-latest",
    generation_config={
        "temperature": 0,
        "top_p": 1,
        "top_k": 1
    }
)

role_keywords = {
    "Software Engineer": ["DSA", "OOP", "APIs", "Git", "Testing"],
    "Frontend Developer": ["HTML", "CSS", "JavaScript", "React", "UI"],
    "Backend Developer": ["APIs", "Databases", "Python", "Node.js", "Security"],
    "Full Stack Developer": ["Frontend", "Backend", "APIs", "Databases", "Deployment"],
    "Data Analyst": ["SQL", "Excel", "Power BI", "Python", "Statistics"],
    "Data Scientist": ["Python", "ML", "Statistics", "Pandas", "Numpy"],
    "Machine Learning Engineer": ["ML", "Deep Learning", "TensorFlow", "PyTorch"],
    "DevOps Engineer": ["Docker", "Kubernetes", "CI/CD", "AWS", "Linux"],
    "Cloud Engineer": ["AWS", "Azure", "GCP", "Networking", "Security"],
    "UI/UX Designer": ["Figma", "User Research", "Wireframes", "Prototyping"],
    "Product Manager": ["Roadmap", "Stakeholders", "Agile", "KPIs"],
    "Business Analyst": ["Requirements", "Documentation", "Stakeholders", "Process Mapping"]
}

company_roles = {
    "Google": ["Software Engineer", "Frontend Developer", "Backend Developer", "Data Scientist", "Machine Learning Engineer"],
    "Microsoft": ["Software Engineer", "Cloud Engineer", "DevOps Engineer", "Product Manager"],
    "Amazon": ["Software Engineer", "Backend Developer", "Cloud Engineer", "Data Analyst"],
    "Meta": ["Frontend Developer", "Backend Developer", "Data Scientist"],
    "Apple": ["iOS Developer", "UI/UX Designer", "Software Engineer"],
    "Tesla": ["Machine Learning Engineer", "Robotics Engineer", "Software Engineer"],
    "Netflix": ["Backend Developer", "Data Engineer"],
    "Adobe": ["Frontend Developer", "UI/UX Designer"],
    "IBM": ["Backend Developer", "Cloud Engineer"],
    "Intel": ["Embedded Systems Engineer", "Hardware Engineer"]
}

general_keywords = ["Communication", "Teamwork", "Problem Solving", "Git", "APIs", "Python", "Databases"]

def extract_text(file):
    if file.filename.endswith(".pdf"):
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    elif file.filename.endswith(".docx"):
        doc = docx.Document(file)
        return "\n".join([p.text for p in doc.paragraphs])
    else:
        return None

@app.route("/", methods=["GET"])
def home():
    return render_template(
        "index.html",
        history=session.get("history", []),
        score=None,
        strengths=[],
        improvements=[],
        feedback="",
        match_percent=0,
        found_keywords=[],
        missing_keywords=[],
        company=None,
        job_role=None
    )

def keyword_match(resume_text, keywords):
    resume_text = resume_text.lower()
    found = []
    missing = []

    for kw in keywords:
        if kw.lower() in resume_text:
            found.append(kw)
        else:
            missing.append(kw)

    total = len(keywords)
    match_percent = int((len(found) / total) * 100) if total > 0 else 0

    return match_percent, found, missing


@app.route("/analyze", methods=["POST"])
def analyze():
    company = request.form.get("company")
    job_role = request.form.get("job_role")

    custom_company = request.form.get("custom_company")
    custom_job_role = request.form.get("custom_job_role")

    # If user typed custom values, override dropdown
    if custom_company and custom_company.strip():
        company = custom_company.strip()

    if custom_job_role and custom_job_role.strip():
        job_role = custom_job_role.strip()


    keywords = role_keywords.get(job_role, general_keywords)


    file = request.files.get("resume")
    if not file:
        return render_template(
            "index.html",
            history=session.get("history", []),
            error="❌ Please upload your resume file.",
            score=None,
            strengths=[],
            improvements=[],
            feedback="",
            match_percent=0,
            found_keywords=[],
            missing_keywords=[]
        )

    text = extract_text(file)
    match_percent, found_keywords, missing_keywords = keyword_match(text, keywords)

    if not text:
        return render_template(
            "index.html",
            history=session.get("history", []),
            error="❌ Could not read text from your resume file.",
            score=None,
            strengths=[],
            improvements=[],
            feedback="",
            match_percent=0,
            found_keywords=[],
            missing_keywords=[]
        )


    prompt = f"""
You are an ATS resume analyzer.

The candidate is applying for:
Company: {company}
Job Role: {job_role}

Important keywords for this role:
{", ".join(keywords)}

Evaluate the resume strictly and consistently for this specific company and role.

Rules:
- Always score using the same criteria.
- Score must be an integer from 0 to 100.
- Score based on: formatting, skills, clarity, relevance, impact for the selected role.
- Be deterministic and consistent.
- Do NOT use markdown like ** or *
- For point titles, wrap them in <b>...</b> HTML tags

Output format:
SCORE: <number>

STRENGTHS:
- <b>Point title:</b> description
- <b>Point title:</b> description
- <b>Point title:</b> description

IMPROVEMENTS:
- <b>Point title:</b> description
- <b>Point title:</b> description
- <b>Point title:</b> description

OVERALL FEEDBACK:
2–3 lines of summary advice.

Resume:
{text}
"""


    from google.api_core.exceptions import ResourceExhausted

    try:
        response = model.generate_content(prompt)
        result = response.text
    except ResourceExhausted:
        return render_template(
        "index.html",
        result="⚠️ Daily AI quota exceeded. Please try again tomorrow.",
        history=session.get("history", []),
    )


    import re

    # Extract score
    raw_result = response.text

    score_match = re.search(r'SCORE:\s*(\d{1,3})', raw_result)
    score = int(score_match.group(1)) if score_match else None
    if score is not None:
        score = max(0, min(score, 100))  # Clamp 0–100

    result = raw_result


    def extract_section(text, start, end=None):
        try:
            if end:
                pattern = rf"{start}:\s*(.*?){end}:"
                match = re.search(pattern, text, re.S | re.I)
            else:
                pattern = rf"{start}:\s*(.*)"
                match = re.search(pattern, text, re.S | re.I)

            if not match:
                return []

            lines = match.group(1).strip().split("\n")
            clean_lines = []

            for line in lines:
                line = line.strip()
                if line.startswith("-"):
                    clean_lines.append(line)
            return clean_lines
        except:
            return []

    # Extract sections safely
    strengths_list = extract_section(result, "STRENGTHS", "IMPROVEMENTS")
    improvements_list = extract_section(result, "IMPROVEMENTS", "OVERALL FEEDBACK")

    feedback_match = re.search(r'OVERALL FEEDBACK:\s*(.*)', result, re.S | re.I)
    feedback = feedback_match.group(1).strip() if feedback_match else "No feedback generated."


    try:
        if "history" not in session:
            session["history"] = []
    except:
        session.clear()
        session["history"] = []

    session["history"].insert(0, {
        "filename": file.filename,
        "company": company,
        "job_role": job_role,
        "score": score,
        "time": datetime.now().strftime("%d %b %Y %H:%M")
    })

    session.modified = True

    return render_template (
        "index.html",
        score=score,
        strengths=strengths_list,
        improvements=improvements_list,
        feedback=feedback,
        history=session.get("history", []),
        company=company,
        job_role=job_role,
        match_percent=match_percent,
        found_keywords=found_keywords,
        missing_keywords=missing_keywords
    )


@app.route("/download_pdf", methods=["POST"])
def download_pdf():
    score = request.form.get("score")
    company = request.form.get("company")
    job_role = request.form.get("job_role")
    strengths = request.form.get("strengths")
    improvements = request.form.get("improvements")
    feedback = request.form.get("feedback")

    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=30)

    styles = getSampleStyleSheet()
    title_style = styles["Heading1"]
    normal = styles["BodyText"]

    # Remove HTML tags like <b>
    def clean_text(text):
        return re.sub(r"<.*?>", "", text or "")

    elements = []

    elements.append(Paragraph("AI Resume Analyzer Report", title_style))
    elements.append(Spacer(1, 12))

    info_table = Table([
        ["Company", company],
        ["Job Role", job_role],
        ["Score", f"{score}%"]
    ], colWidths=[120, 350])

    info_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('PADDING', (0,0), (-1,-1), 8),
    ]))

    elements.append(info_table)
    elements.append(Spacer(1, 15))

    elements.append(Paragraph("<b>STRENGTHS</b>", styles["Heading2"]))
    for line in clean_text(strengths).split("\n"):
        elements.append(Paragraph(line, normal))

    elements.append(Spacer(1, 10))

    elements.append(Paragraph("<b>IMPROVEMENTS</b>", styles["Heading2"]))
    for line in clean_text(improvements).split("\n"):
        elements.append(Paragraph(line, normal))

    elements.append(Spacer(1, 10))

    elements.append(Paragraph("<b>OVERALL FEEDBACK</b>", styles["Heading2"]))
    elements.append(Paragraph(clean_text(feedback), normal))

    doc.build(elements)
    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name="resume_analysis_report.pdf",
        mimetype="application/pdf"
    )

@app.route("/test-session")
def test_session():
    session["test"] = "ok"
    return "Session is working"

if __name__ == "__main__":
    app.run(debug=True)

