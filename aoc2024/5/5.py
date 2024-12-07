from aoc2024 import getInput


def get_middle_element(elements):
    middle_index = len(elements) // 2
    return elements[middle_index]


all_lines = getInput.get_input_lines()
rules = []
updates = []
for i in all_lines:
    if "|" in i:
        rules.append(i.strip())
    else:
        updates.append(i.strip())
del updates[0]

valid_updates = []
rules = list([(i.split("|")[0], i.split("|")[1]) for i in rules])
for update in updates:
    valid_for_now = True
    for x, y in rules:
        if x in update and y in update:
            if update.index(x) >= update.index(y):
                valid_for_now = False
                break
    if valid_for_now:
        valid_updates.append(list(map(int, update.split(","))))

print(f'Part 1: {sum([get_middle_element(i) for i in valid_updates])}')
