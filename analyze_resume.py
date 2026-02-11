from google import genai

client = genai.Client(api_key="AIzaSyD9Src8JJqZ_D5X0XHl5oluN23KVjiDk6Q")

# Read resume file
with open("resume.txt", "r", encoding="utf-8") as f:
    resume_text = f.read()

prompt = f"""
You are a resume analyzer.
Analyze the resume below and give:
1. Resume score out of 100
2. Missing skills for Web Developer
3. Suggestions to improve

Resume:
{resume_text}
"""

response = client.models.generate_content(
    model="models/gemini-2.5-flash",
    contents=prompt
)

print(response.text)
