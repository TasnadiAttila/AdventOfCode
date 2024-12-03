from aoc2024 import getInput

lines = getInput.get_input_lines()

#Part 1

left_list = sorted(map(int, [i.split()[0]for i in lines]))
right_list = sorted(map(int, [i.split()[1] for i in lines]))

distance = 0
for i in range(len(left_list)):
    distance += abs(right_list[i] - left_list[i])

print(f'Part 1: {distance}')

#Part 2

collector = 0
for i in range(len(left_list)):
    appearance = right_list.count(left_list[i])
    collector += appearance * left_list[i]

print(f'Part 2: {collector}')





