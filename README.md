# Jobique: Cold Email & Cover Letter Generator

This is a web application that helps job seekers generate personalized cold emails and cover letters using AI technology. The application uses Flask for the backend, Google Gemini API for content generation, and Tailwind CSS for frontend styling. It is further deployed on Render.

You can access it here: [Jobique](https://jobique.onrender.com)

## Features
- **Upload job posting link**: Allows users to input a job posting URL.
- **Upload resume (PDF)**: Users can upload their resume in PDF format for tailored email and cover letter generation.
- **Generate personalized cold email**: Uses AI to craft a cold email based on the job description and resume.
- **Generate tailored cover letter**: Automatically generates a cover letter that matches the job posting and user's qualifications.
- **User-friendly interface**: Clean, modern UI built with Tailwind CSS.

## Technology Stack
- **Backend**: Flask (Python)
- **Frontend**: HTML, JavaScript, Tailwind CSS
- **AI Generation**: Google Gemini API
- **PDF Parsing**: PyPDF2
- **Environment Management**: Python Virtual Environment
- **Frontend Build Tools**: Node.js, npm, Tailwind CSS

## Prerequisites
Before you begin, ensure you have the following installed:
- **Python** (3.8+)
- **Node.js** (14+)
- **pip** (for Python package installation)
- **npm** (for frontend dependencies)

You can download Python from [python.org](https://www.python.org/) and Node.js from [nodejs.org](https://nodejs.org/).

## Setup Instructions

### Clone the Repository
```bash
git clone https://github.com/yourusername/cold-email-generator.git
cd cold-email-generator
```

### Backend Setup

#### Create a Virtual Environment
```bash
python -m venv venv
```
On Windows, activate the virtual environment:
```bash
venv\Scripts\activate
```

#### Install Python Dependencies
Make sure your virtual environment is activated, then run:
```bash
pip install -r requirements.txt
```

#### Set Up Environment Variables
Create a `.env` file in the root directory of the project and add your Google Gemini API key:
```ini
GEMINI_API_KEY=your_google_gemini_API_key
```

### Frontend Setup

#### Install Node.js Dependencies
Navigate to the frontend directory:
```bash
cd frontend
npm install
```

#### Build Tailwind CSS
Compile the Tailwind CSS before running the application:
```bash
npm run build:css
```

## Running the Application

### Start Backend Server
In the root project directory, run:
```bash
python -m backend.app
```
or run using the following command
```bash
flask --app backend.app run --reload
```
This will start the Flask server, accessible at `http://localhost:5000`.

### Optional: Watch Tailwind CSS (Frontend)
In a separate terminal window, navigate to the frontend directory and run:
```bash
npm run watch:css
```

### Access the Application
Open your browser and navigate to:
```text
http://localhost:5000
```
You should now see the application running locally!

## Configuration

### Tailwind CSS Configuration
- **Configuration file**: `tailwind.config.js`
- **Input CSS file**: `frontend/src/input.css`
- **Output CSS file**: `frontend/output.css`
- **PostCSS file**:`postcss.config.js`

### Backend Configuration
- **Main application file**: `backend/app.py`
- **Utility functions**: `backend/utils.py`
- **AI generation logic**: `backend/genai_utils.py`
- **PDF parsing utility**: `backend/utils.py`

## API Integration
This application uses the Google Gemini API for generating personalized cold emails and cover letters. Replace the `GEMINI_API_KEY` in the `.env` file with your own API key from Google Gemini.

Refer to [Google's API documentation](https://developers.google.com/) for more details on obtaining your API key.
