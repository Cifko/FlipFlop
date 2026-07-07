# type:ignore

lines = [l.strip() for l in open("05.txt").readlines()]

part1 = part2 = part3 = 0

line = lines[0]

tunnels = {}

not_visited = set(line)

for i, c in enumerate(line):
    if c not in tunnels:
        tunnels[c] = []
    tunnels[c].append(i)

i = 0
while i < len(line):
    c = line[i]
    if c in not_visited:
        not_visited.remove(c)
    ni = sum(tunnels[c]) - i
    part1 += abs(ni - i)
    if c.upper() == c:
        part3 -= abs(ni - i)
    else:
        part3 += abs(ni - i)
    i = ni + 1

part2 = ""
for c in line:
    if c in not_visited:
        part2 += c
        not_visited.remove(c)

print("Part1", part1)
print("Part2", part2)
print("Part3", part3)
