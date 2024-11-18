import os

file_path = os.path.join(os.path.dirname(__file__), 'main.txt')
with open(file_path, "r") as file:
    lines = [line.strip() for line in file]

gamma_rate = []
epsilon_rate = []

for j in range(len(lines[0])):
    bit_column = [int(line[j]) for line in lines]
    gamma_rate.append(0 if bit_column.count(0) > bit_column.count(1) else 1)
    epsilon_rate.append(0 if bit_column.count(0) < bit_column.count(1) else 1)

gamma_in_dec = int(''.join(map(str, gamma_rate)), 2)
epsilon_in_dec = int(''.join(map(str, epsilon_rate)), 2)

power_consumption = gamma_in_dec * epsilon_in_dec

print(power_consumption)
