lines = [int(line.strip()) for line in open("01.txt").readlines()]

part1 = part2 = part3 = 0

for t in lines:
    part1 += max(0, 60 - t)
    part2 += max(0, 60 - t) + 5 * max(0, t - 60)

for t, p in zip(lines[: len(lines) // 2], lines[len(lines) // 2 :]):
    part3 += max(0, p - t) + 5 * max(0, t - p)

print("Part1", part1)
print("Part2", part2)
print("Part3", part3)
