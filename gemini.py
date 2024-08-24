import google.generativeai as genai # type: ignore
import os

api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
    raise ValueError("API key not found. Make sure 'GEMINI_API_KEY' is set in your environment variables.")

genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

def generate(prompt: str) -> str:
    response = model.generate_content(f"Do not use markdown or HTML tags as your response will be shown in a console. Return only the text. Here is your prompt: {prompt}")
    return response.text