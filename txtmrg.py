import os
def merge_text_files(input_files, output_file):
    with open(output_file, 'a', encoding='utf-8') as output:
        for input_file in input_files:
            try:
                with open(f"output/{input_file}", 'r', encoding='utf-8') as file:
                    content = file.read()
                    output.write(content + '\n\n')  # Add a newline between file contents
            except FileNotFoundError:
                print(f"File not found: {input_file}")
            except Exception as e:
                print(f"Error reading file {input_file}: {e}")
                
                
def sort(text_files):
    text_files.sort(key=lambda x: int(x.split(".")[0].split("_")[1]))

    return text_files
              
text_files = os.listdir("output")
input_files = sort(text_files)
output_file = 'combined_output.txt'

merge_text_files(input_files, output_file)
print(f"Contents from {len(input_files)} files merged into {output_file}")