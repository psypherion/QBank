import google.generativeai as genai
import PIL.Image

GOOGLE_API_KEY = "AIzaSyDX-tFjDHHGyNVPRBSRWDc0mK-UW29JleQ"

genai.configure(api_key=GOOGLE_API_KEY)
for models in genai.list_models():
    if 'generateContent' in models.supported_generation_methods:
        print(models.name)
        
        
model = genai.GenerativeModel('gemini-pro-vision')

img = PIL.Image.open("temp/page_3.png")
response = model.generate_content(img, stream=True)
response.resolve()
print(response.text)