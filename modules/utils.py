# pages/utils.py
from huggingface_hub import InferenceClient
import PyPDF2
import docx
import os
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
# repo_id = os.getenv("repo_id")
repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"

llm_client = InferenceClient(
    model=repo_id,
    token=HF_TOKEN,
    timeout=120,
)

def call_llm(inference_client: InferenceClient, prompt: str):
    response = inference_client.text_generation(
        prompt=prompt,
        max_new_tokens=1000
    )
    if isinstance(response, str):
        return response
    else:
        return response[0]["generated_text"]

# Đọc file .txt
def read_text_file(file):
    return file.read().decode("utf-8")

# Đọc file PDF
def read_pdf_file(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Đọc file .docx
def read_docx_file(file):
    doc = docx.Document(file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text