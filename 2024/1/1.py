import os

file_path = os.path.join(os.path.dirname(__file__), '1.txt')
with open(file_path, "r") as file:
    lines = [line.strip() for line in file]

left_list = sorted(map(int, [i.split()[0]for i in lines]))
right_list = sorted(map(int, [i.split()[1] for i in lines]))

distance = 0
for i in range(len(left_list)):
    distance += abs(right_list[i] - left_list[i])

print(distance)





