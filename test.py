import google.generativeai as genai
import PIL.Image
import os
GOOGLE_API_KEY = "AIzaSyDX-tFjDHHGyNVPRBSRWDc0mK-UW29JleQ"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro-vision')


def sorted_images(path):
    sorted_paths = []
    sorted_img = sorted(os.listdir(path), key=lambda x: int(x.split('.')[0].split('_')[1]))
    for img in sorted_img:
        i = os.path.join(path, img)
        sorted_paths.append(i)
    return sorted_paths

sorted_img_paths = sorted_images('temp/')

def content(img_path, prompt):
    img = PIL.Image.open(img_path)
    print("image has been read")
    response = model.generate_content(img, stream=True)
    print("Response generated")
    response.resolve()
    print("Response has been resolved")
    return response

prompt = "What's the questions and answers mention in the image?"

for i in sorted_img_paths:
    print("Now calling content function")
    content = content(i, prompt)
    print(content)
    with open('test.txt', 'a', encoding='utf-8') as file:
        file.write(content)