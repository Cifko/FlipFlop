lines = open("01.txt").readlines()

part1 = part2 = part3 = 0
for line in lines:
    x = line.count("ba") + line.count("na") + line.count("ne")
    part1 += x
    if x % 2 == 0:
        part2 += x
    if "ne" not in line:
        part3 += x

print("Part1", part1)
print("Part2", part2)
print("Part3", part3)
