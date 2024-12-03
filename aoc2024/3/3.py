from aoc2024 import getInput
import re

lines = getInput.get_input_lines()

#Part 1
mul = r"mul\((\d{1,3}),(\d{1,3})\)"
counter = 0
counter += sum(int(x) * int(y) for line in lines for x, y in re.findall(mul, line))
print(f'Part 1: {counter}')

#Part 2
#Im cooked