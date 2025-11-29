# ATS-Resume-Analyzer-
Created an AI-driven tool to analyze resumes using Python, Streamlit, and Google Gemini. Handled PDF uploads with pdf2image &amp; Poppler and deployed the app globally via Streamlit Cloud.
---
Architecture 
[Architecture ](https://github.com/brunda-yadav/ATS-Resume-Analyzer-/blob/main/Architecture%20Diagram%20.png)

---
Overview
- The AI Resume ScreeningAgent is a Streamlit-based tool that analyzes and ranks resumes using a provided Job Description (JD).
- It extracts text from PDF resumes, uses an LLM to evaluate skills, experience, role fit, and generates an ATS-style match score.
- The tool helps recruiters or HR teams quickly identify the most suitable candidates.
---
Features
- Calculates match percentage
- Highlights missing keywords
- Gives improvement suggestions
---
Limitations
- Works only with PDF resumes
- No built-in database or user management
---
Tech Stack & APIs Used
- Programming & Frameworks
- Python 3.10+
- Streamlit – UI web app
- PyPDF2 – PDF text extraction
- dotenv – Manage API keys
---
AI / LLM API
- Groq LLM API (Ultra-fast inference)
- Used to analyze resumes
- Evaluate JD match
---
Setup & Run Instructions

1️⃣ Clone the Repository
- git clone https://github.com/brunda-yadav/ai-resume-screening-agent.git
cd ai-resume-screening-agent

2️⃣ Create Virtual Environment
- python -m venv venv

3️⃣ Activate Environment (Windows)
- venv\Scripts\activate

4️⃣ Install Dependencies
- pip install -r requirements.txt

5️⃣ Add Your API Key

- Create a file named .env and add:

GROQ_API_KEY=your_api_key_here

6️⃣ Run the App
- streamlit run ats.py


The application will open in your browser.
---
Potential Improvements
- Add PDF report generation of analysis
- Add a dashboard for recruiters
- Add database support (MongoDB / Firebase)
- Add visual charts (keyword match graphs)
