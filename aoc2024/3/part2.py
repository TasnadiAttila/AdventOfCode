from re import findall, compile
data = open("input.txt").read()
mul_pattern = compile(r"mul\((\d+),(\d+)\)")

data = " ".join(part.split("don't()")[0] for part in data.split("do()"))
print("Part 2:", sum(int(g[0])*int(g[1]) for g in findall(mul_pattern, data)))