import os

file_path = os.path.join(os.path.dirname(__file__), 'main.txt')
with open(file_path, "r") as file:
    lines = [line.strip() for line in file]

starting_depth = 0
horizontal_pos = 0

command_actions = {
    "forward": lambda x: (0, int(x)),
    "down": lambda x: (int(x), 0),
    "up": lambda x: (-int(x), 0)
}

for command in lines:
    direction, value = command.split()
    depth_change, horizontal_change = command_actions[direction](value)
    starting_depth += depth_change
    horizontal_pos += horizontal_change

print(f'Horizontal pos: {horizontal_pos} - Depth: {starting_depth}. Total: {starting_depth*horizontal_pos}')
