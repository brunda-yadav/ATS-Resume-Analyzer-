import os
import base64
import streamlit as st
import io
from PIL import Image
import pdf2image
import google.generativeai as genai
from dotenv import load_dotenv

# -------------------------------
# Load environment variables from .ats
load_dotenv(".ats")  # Rename your environment file to .ats

# Configure Google Generative AI API key
API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)

# Poppler path for PDF conversion
POPPLER_PATH = os.getenv("POPPLER_PATH")

# -------------------------------
# Function to get response from Gemini
def get_gemini_response(job_description, pdf_content, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([job_description, pdf_content[0], prompt])
    return response.text

# -------------------------------
# Convert PDF to images and encode as base64
def prepare_pdf(uploaded_file):
    if uploaded_file is not None:
        images = pdf2image.convert_from_bytes(
            uploaded_file.read(),
            poppler_path=POPPLER_PATH
        )
        first_page = images[0]

        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format="JPEG")
        img_bytes = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_bytes).decode()
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No resume file was uploaded!")

# -------------------------------
# Streamlit UI
st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Resume Analyzer")

job_description = st.text_area("Paste the job description here:", key="input")
uploaded_file = st.file_uploader("Select your Resume (PDF) to upload:", type=["pdf"])

if uploaded_file is not None:
    st.success("Resume uploaded successfully!")

btn_review = st.button("Analyze Resume")
btn_match = st.button("Check Match Percentage")

# -------------------------------
# Prompts for Gemini model
prompt_review = """
You are a seasoned Technical HR professional. 
Review the uploaded resume in light of the job description. 
Provide insights on the candidate’s strengths, areas for improvement, and fit for the role.
"""

prompt_match = """
You are an expert in ATS evaluation. 
Analyze the resume against the job description. 
Give a compatibility score, point out missing skills or keywords, and provide a concise summary.
"""

# -------------------------------
# Button actions
if btn_review:
    if uploaded_file:
        pdf_data = prepare_pdf(uploaded_file)
        response = get_gemini_response(prompt_review, pdf_data, job_description)
        st.subheader("Resume Analysis")
        st.write(response)
    else:
        st.warning("Please upload a resume before analysis.")

elif btn_match:
    if uploaded_file:
        pdf_data = prepare_pdf(uploaded_file)
        response = get_gemini_response(prompt_match, pdf_data, job_description)
        st.subheader("Resume Match Percentage")
        st.write(response)
    else:
        st.warning("Please upload a resume to calculate the match percentage.")
