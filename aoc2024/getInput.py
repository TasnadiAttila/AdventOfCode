def get_input_lines():
    import os
    current_dir = os.path.basename(os.getcwd())
    file_path = os.path.join(os.getcwd(), 'input.txt')
    with open(file_path, "r") as file:
        return [line for line in file]
