# type:ignore

lines = [l.strip() for l in open("06.txt").readlines()]

part1 = part2 = part3 = 0

for line in lines:
    x, y = map(int, line.split(","))
    for s in range(1, 1001):
        px = x * s * 3600
        py = y * s * 3600
        px %= 1000
        py %= 1000
        if 750 > px >= 250 and 750 > py >= 250:
            part2 += 1
        px = x * s * 31556926
        py = y * s * 31556926
        px %= 1000
        py %= 1000
        if 750 > px >= 250 and 750 > py >= 250:
            part3 += 1
    x *= 100
    y *= 100
    x %= 1000
    y %= 1000
    if 750 > x >= 250 and 750 > y >= 250:
        part1 += 1

print("Part1", part1)
print("Part2", part2)
print("Part3", part3)
