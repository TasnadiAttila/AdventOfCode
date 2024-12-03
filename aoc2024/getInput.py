import os

def get_input_lines():
    current_dir = os.path.basename(os.getcwd())
    file_path = os.path.join(os.getcwd(), 'input.txt')
    with open(file_path, "r") as file:
        return [line.strip() for line in file]
