from sys import prefix

from aoc2024 import getInput
import re

lines = getInput.get_input_lines()

#Part 1
mul = r"mul\((\d{1,3}),(\d{1,3})\)"
print(f'Part 1: {sum(int(x) * int(y) for line in lines for x, y in re.findall(mul, line))}')

#Part 2
#Im cooked
