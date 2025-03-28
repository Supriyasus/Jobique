import PyPDF2
import requests
from bs4 import BeautifulSoup

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = " ".join(page.extract_text() for page in reader.pages if page.extract_text())
    return text if text else "Unable to extract text."

def scrape_job_details(job_link):
    response = requests.get(job_link)
    if response.status_code != 200:
        return "Unknown Title", "Unknown Company", "No Description", "No Company Info"

    soup = BeautifulSoup(response.text, "html.parser")

    job_title = soup.find("h1").text.strip() if soup.find("h1") else "Unknown Title"
    company_name = soup.find("div", class_="company-name").text.strip() if soup.find("div", class_="company-name") else "Unknown Company"
    job_description = soup.find("div", class_="job-description").text.strip() if soup.find("div", class_="job-description") else "No Description"
    company_info = soup.find("div", class_="company-info").text.strip() if soup.find("div", class_="company-info") else "No Company Info"

    return job_title, company_name, job_description, company_info
