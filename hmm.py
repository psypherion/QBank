import google.generativeai as genai
import PIL.Image
import os

GOOGLE_API_KEY = "AIzaSyAn_7Upa5W0r2VA-BszlEP_QisycK7i9_0"
genai.configure(api_key=GOOGLE_API_KEY)

prompt = """
Extract the question and answer sections only from the provided image, omitting any extraneous information like headers, footers, page numbers, or decorative elements. 
Ensure the answer directly follows its corresponding question, adhering to a clear question-answer format.
Present the extracted content in a well-structured manner, separating each question-answer pair with a clear delimiter or numbering system for easy identification.
"""

for i in range(2, 48):
    img = PIL.Image.open(f'temp/page_{i}.png')
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([prompt, img], stream=True)
    response.resolve()  
    with open(f'gate-refined.txt', 'a', encoding='utf-8') as file:
        file.write(response.text)
    
    print(f"Question no {i-1} written successfully")