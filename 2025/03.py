from collections import Counter

lines = [l.strip() for l in open("03.txt").readlines()]

part1 = part2 = part3 = 0
part1 = Counter(lines).most_common(1)[0][0]

for line in lines:
    r, g, b = map(int, line.split(","))
    if g > r and g > b and r != b:
        part2 += 1
        part3 += 2
    elif r > g and r > b and g != b:
        part3 += 5
    elif b > r and b > g and r != g:
        part3 += 4
    else:
        part3 += 10

print("Part1", part1)
print("Part2", part2)
print("Part3", part3)
