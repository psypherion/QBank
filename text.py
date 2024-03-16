import os
import sys
import subprocess


image_list = os.listdir("temp")
def sort(image_list):
    image_list.sort(key=lambda x: int(x.split(".")[0].split("_")[1]))

    return image_list


def sort(text_files):
    text_files.sort(key=lambda x: int(x.split(".")[0].split("_")[1]))

    return text_files

def merge_text_files(input_files, output_file):
    with open(output_file, 'a', encoding='utf-8') as output:
        for input_file in input_files:
            try:
                with open(input_file, 'r', encoding='utf-8') as file:
                    content = file.read()
                    output.write(content + '\n\n')  # Add a newline between file contents
            except FileNotFoundError:
                print(f"File not found: {input_file}")
            except Exception as e:
                print(f"Error reading file {input_file}: {e}")
                
                
if __name__ == "__main__":
        # Replace these file paths with the paths to your input files and the desired output file
        
    sorted_img_list = sort(image_list)

    count = 0
    for images in sorted_img_list:
        print(images)
        count += 1
        subprocess.run(["ocrs", f"temp/{images}", "-o", f"output/output_{count}.txt"], capture_output=True)
        
    text_files = os.listdir("output")
    input_files = sort(text_files)
    output_file = 'combined_output.txt'

    merge_text_files(input_files, output_file)
    print(f"Contents from {len(input_files)} files merged into {output_file}")