# type:ignore
line = open("02.txt").readline()

part1 = part2 = part3 = 0

wall1 = [0] * 100
wall3 = [0] * 100
wp = 0
p = 0
for c, d in zip(line, line[::-1]):
    if c == ">":
        p += 1
    else:
        p -= 1
    if d == ">":
        wp += 1
    else:
        wp -= 1
    wall1[p % 100] += 1
    wall3[(p - wp) % 100] += 1
    if wp % 100 == p % 100:
        part2 += 1

part1 = (1 + wall1.index(max(wall1))) * max(wall1)
part3 = (1 + wall3.index(max(wall3))) * max(wall3)

print("Part1", part1)
print("Part2", part2)
print("Part3", part3)
