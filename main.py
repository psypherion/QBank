from ocr_handler import OCRHandler
from pdf_splitter import PDFSplitter

if __name__ == "__main__":
    # Initialize OCR Handler
    GOOGLE_API_KEY = "AIzaSyA9gMhubjxQ4DztNamQcuSjhAse-ePi-EY"
    ocr_handler = OCRHandler(GOOGLE_API_KEY)    Extract the question and answer sections only from the provided image, omitting any extraneous information like headers, footers, page numbers, or decorative elements. 

# Convert the PDF to images
    input_pdf_path = "src/gate.pdf"
    output_folder_path = "temp/"
    pdf_splitter = PDFSplitter(input_pdf_path)
    pdf_splitter.pdf_to_images(output_folder_path)
    print("Conversion completed. Images saved in the output folder.")
    # Initialize PDF Splitter
    

    # Perform OCR on each page and write the extracted text to a file
    prompt = """
    Extract the question and answer sections only from the provided image, omitting any extraneous information like headers, footers, page numbers, or decorative elements. 
    Ensure the answer directly follows its corresponding question, adhering to a clear question-answer format.
    Present the extracted content in a well-structured manner, separating each question-answer pair with a clear delimiter or numbering system for easy identification.
    """
    for i in range(1, 48):
        image_path = f'temp/page_{i}.png'
        extracted_text = ocr_handler.extract_text(prompt, image_path)
        with open(f'gate-refined.txt', 'a', encoding='utf-8') as file:
            file.write(extracted_text)
        print(f"Text extracted from page {i} and written successfully")

    
