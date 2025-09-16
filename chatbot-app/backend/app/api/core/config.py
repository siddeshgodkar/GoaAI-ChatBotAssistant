import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# print("DEBUG: GROQ_API_KEY =", GROQ_API_KEY)
# MAPPLS_API_KEY = os.getenv("MAPPLS_API_KEY")
LLAMA_API_URL = os.getenv("LLAMA_API_URL")
# print("DEBUG: LLAMA_API_URL =", LLAMA_API_URL)
