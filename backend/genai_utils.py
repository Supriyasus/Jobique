import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

# Get the access token from the environment variable
API_KEY = os.getenv("ACCESS_TOKEN")
genai.configure(api_key=API_KEY)

def generate_text(prompt):
    """Helper function to call Google Gemini API"""
    response = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt)
    return response.text if response else "Error generating text."

def generate_email_and_cover_letter(resume_text, job_title, company_name, job_description, company_info, additional_info):
    """Generate both a concise and impactful cold email and cover letter using Gemini"""

    # Cold Email Prompt
    email_prompt = f"""
    Write a concise,humanized and professional cold email to apply for the {job_title} position at {company_name}.
    - Extract only the most relevant qualifications and experiences from the resume.
    - Focus on how my skills match the job requirements.
    - Keep the email polite, engaging, and to the point (5-6 sentences max).
    - End with a strong call to action.
    
    **Job Details (extract key aspects only):**
    {job_description}

    **Company Insights (only relevant details):**
    {company_info}

    **Resume Highlights (most relevant skills/experience only):**  
    {resume_text}

    **Additional Context:**  
    {additional_info}
    """
    cold_email = generate_text(email_prompt)

    # Cover Letter Prompt
    cover_letter_prompt = f"""
    Write a concise,humanized and compelling cover letter for the {job_title} position at {company_name}.
    - Extract only the most critical details that align with the role.
    - Keep it well-structured, clear, and impactful.
    - Avoid generic statements; provide specific skills and achievements.
    - Maximum length: 3 short paragraphs.
    
    **Job Summary (key requirements only):**
    {job_description}

    **Company Overview (only relevant details):**
    {company_info}

    **Resume Summary (highlight the best matching qualifications):**  
    {resume_text}

    **Additional Information (if relevant):**  
    {additional_info}


    """
    cover_letter = generate_text(cover_letter_prompt)

    return cold_email, cover_letter

