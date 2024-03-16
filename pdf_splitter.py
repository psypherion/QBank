import fitz
from PIL import Image
import os

class PDFSplitter:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def pdf_to_images(self, output_folder):
        pdf_document = fitz.open(self.pdf_path)
        for page_number in range(pdf_document.page_count):
            page = pdf_document[page_number]
            rect = page.rect
            image = page.get_pixmap(matrix=fitz.Matrix(300 / 72, 300 / 72))
            pil_image = Image.frombytes("RGB", [image.width, image.height], image.samples)
            image_filename = f"{output_folder}/page_{page_number + 1}.png"
            pil_image.save(image_filename)
        pdf_document.close()

    def pdf_size(self):
        pdf_document = fitz.open(self.pdf_path)
        pdf_size = pdf_document.page_count
        pdf_document.close()
        return pdf_size
    
if __name__ == "__main__":
    pdf_splitter = PDFSplitter()
    input_pdf_path = "src/gate.pdf"
    output_folder_path = "temp/"
    os.makedirs(output_folder_path, exist_ok=True)
    pdf_splitter.pdf_to_images(input_pdf_path, output_folder_path)
    print("Conversion completed. Images saved in the output folder.")
