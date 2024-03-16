import fitz
from PIL import Image
import os

def pdf_to_images(pdf_path, output_folder):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    # Iterate through each page in the PDF
    for page_number in range(pdf_document.page_count):
        # Get the current page
        page = pdf_document[page_number]
        # Get the dimensions of the page
        rect = page.rect
        # Convert the page to an image
        image = page.get_pixmap(matrix=fitz.Matrix(300 / 72, 300 / 72))
        # Create a PIL Image object from the image data
        pil_image = Image.frombytes("RGB", [image.width, image.height], image.samples)
        # Save the image to the output folder
        image_filename = f"{output_folder}/page_{page_number + 1}.png"
        pil_image.save(image_filename)
    # Close the PDF document
    pdf_document.close()

if __name__ == "__main__":
    # Specify the input PDF file and output folder
    input_pdf_path = "src/gate.pdf"
    output_folder_path = "temp/"
    os.makedirs(output_folder_path, exist_ok=True)
    # Convert the PDF to images
    pdf_to_images(input_pdf_path, output_folder_path)
    print("Conversion completed. Images saved in the output folder.")