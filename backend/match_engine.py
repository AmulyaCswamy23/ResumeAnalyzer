
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def compute_similarity(resume_text, job_text):
    emb_resume = model.encode(resume_text, convert_to_tensor=True)
    emb_job = model.encode(job_text, convert_to_tensor=True)
    similarity = util.cos_sim(emb_resume, emb_job).item()
    return round(similarity * 100, 2)
