from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
from backend.utils import extract_text_from_pdf, scrape_job_details
from backend.genai_utils import generate_email_and_cover_letter  # Updated import

app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)

# Check if the app is running on Render or locally
if os.environ.get('RENDER') == 'true':
    # Render environment
    app.config['UPLOAD_FOLDER'] = '/tmp/uploads'  # Use temporary directory in Render
else:
    # Local development environment
    app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)  # Ensure the folder exists

@app.route("/")
def serve_index():
    """Serve the main index.html file."""
    return send_from_directory(app.static_folder, 'index.html')

@app.route("/generate-email", methods=["POST"])
def generate_email():
    """Generate a cold email and cover letter using Google Gemini API."""
    
    job_link = request.form.get("job_link")
    additional_info = request.form.get("additional_info", "")
    resume = request.files.get("resume")

    if not job_link:
        return jsonify({"error": "Job link is required"}), 400

    resume_text = "No resume provided."
    if resume:
        filename = secure_filename(resume.filename)
        resume_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        resume.save(resume_path)
        resume_text = extract_text_from_pdf(resume_path)

    # Scrape job details
    job_title, company_name, job_description, company_info = scrape_job_details(job_link)

    # Generate email and cover letter using Google Gemini
    cold_email, cover_letter = generate_email_and_cover_letter(
        resume_text, job_title, company_name, job_description, company_info, additional_info
    )

    return jsonify({"cold_email": cold_email, "cover_letter": cover_letter})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
