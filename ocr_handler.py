import google.generativeai as genai
import PIL
class OCRHandler:
    def __init__(self, api_key):
        self.api_key = api_key
        genai.configure(api_key=self.api_key)

    def extract_text(self, prompt, image_path):
        model = genai.GenerativeModel('gemini-pro-vision')
        
        img = PIL.Image.open(image_path)
        response = model.generate_content([prompt, img], stream=True)
        response.resolve()
        return response.text

if __name__ == "__main__":
    GOOGLE_API_KEY = "AIzaSyA9gMhubjxQ4DztNamQcuSjhAse-ePi-EY"
    ocr_handler = OCRHandler(GOOGLE_API_KEY)
    prompt = """
    Extract the question and answer sections only from the provided image, omitting any extraneous information like headers, footers, page numbers, or decorative elements. 
    Ensure the answer directly follows its corresponding question, adhering to a clear question-answer format.
    Present the extracted content in a well-structured manner, separating each question-answer pair with a clear delimiter or numbering system for easy identification.
    """
    extracted_text = ocr_handler.extract_text(prompt, 'temp/page_3.png')
    print(extracted_text)