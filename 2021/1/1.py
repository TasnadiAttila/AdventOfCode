with open("main.txt", "r") as file:
    lines = [int(line.strip()) for line in file]

counter = 0
for index, depth in enumerate(lines):
    if index > 0 and lines[index] > lines[index - 1 ]:
        counter += 1
print(counter)