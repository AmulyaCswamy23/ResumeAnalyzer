
import streamlit as st
from backend.resume_parser import extract_text_from_pdf
from backend.job_parser import extract_job_description
from backend.match_engine import compute_similarity
from backend.suggestions import generate_resume_tips
from backend.utils import clean_text
import tempfile

st.set_page_config(page_title="Resume Analyzer", page_icon="📄", layout="centered")

st.title("📄 LinkedIn Resume Analyzer")
st.markdown("Upload your resume and paste a job description to check your match and get improvement suggestions!")

resume_file = st.file_uploader("Upload Your Resume (PDF)", type=["pdf"])
job_text = st.text_area("Paste Job Description Here", height=200)

if st.button("🔍 Analyze"):
    if not resume_file or not job_text.strip():
        st.error("Please upload a resume and paste a job description.")
    else:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(resume_file.read())
            resume_text = extract_text_from_pdf(tmp.name)

        resume_text = clean_text(resume_text)
        job_text_clean = clean_text(job_text)

        with st.spinner("Analyzing..."):
            match_score = compute_similarity(resume_text, job_text_clean)
            suggestions = generate_resume_tips(resume_text, job_text_clean)

        st.subheader("🎯 Match Score")
        st.progress(int(match_score))
        st.success(f"Your resume matches {match_score}% of the job description.")

        st.subheader("💡 Improvement Suggestions")
        st.markdown(f"<div style='background:#f9f9f9;padding:15px;border-radius:10px'>{suggestions}</div>", unsafe_allow_html=True)
