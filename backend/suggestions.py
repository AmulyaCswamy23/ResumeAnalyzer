
from transformers import pipeline

# Load T5 model for simple suggestions
suggestion_model = pipeline("text2text-generation", model="google/flan-t5-small")

def generate_resume_tips(resume_text, job_text):
    prompt = f"How can I improve this resume:\n\n{resume_text}\n\nto better match this job description:\n\n{job_text}"
    result = suggestion_model(prompt, max_length=256, do_sample=True)
    return result[0]['generated_text']
