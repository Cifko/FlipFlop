# type:ignore

lines = [l.strip() for l in open("04.txt").readlines()]

part1 = part2 = part3 = 0

px = py = 0
trash = []
for line in lines:
    x, y = map(int, line.split(","))
    part1 += abs(px - x) + abs(py - y)
    part2 += max(abs(px - x), abs(py - y))
    px, py = x, y
    trash.append((x, y))

px = py = 0
for x, y in sorted(trash, key=lambda x: x[0] + x[1]):
    part3 += max(abs(px - x), abs(py - y))
    px, py = x, y


print("Part1", part1)
print("Part2", part2)
print("Part3", part3)
