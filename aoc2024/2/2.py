from aoc2024 import getInput


def is_increasing(line):
    return all(line[i] < line[i + 1] for i in range(len(line) - 1))


def is_decreasing(line):
    return all(line[i] > line[i + 1] for i in range(len(line) - 1))


lines_as_integers = [list(map(int, line.split())) for line in getInput.get_input_lines()]


def isSafe(line):
    if is_increasing(line) or is_decreasing(line):
        if is_increasing(line):
            if all(line[j + 1] - line[j] in [1, 2, 3] for j in range(len(line) - 1)):
                return True
        if is_decreasing(line):
            if all(line[j] - line[j + 1] in [1, 2, 3] for j in range(len(line) - 1)):
                return True
    else:
        return False


safe_counter1 = 0
safe_counter2 = 0
for line in lines_as_integers:
    if isSafe(line):
        safe_counter1 += 1
        safe_counter2 += 1
    else:
        for j in range(len(line)):
            test_line = list(line)
            del test_line[j]
            if isSafe(test_line):
                safe_counter2 += 1
                break

print(f'Part 1: {safe_counter1}')
print(f'Part 2: {safe_counter2}')
