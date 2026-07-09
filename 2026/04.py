# type:ignore

lines = [line.strip() for line in open("04.txt").readlines()]

part1 = part2 = part3 = 0

while True:
    last_leaf = None
    was_last_left = None
    climbed = False
    for i, line in enumerate(lines):
        if "o" in line:
            if part3 == 0 and i < len(lines) - 400:
                part1 += 1
            is_left = line.startswith("o")
            if was_last_left != None and was_last_left != is_left:
                lines[last_leaf] = lines[last_leaf].replace("o", "x")
                if part3 == 0:  # First climb
                    part2 += 1
            was_last_left = is_left
            last_leaf = i
            climbed = True
    if not climbed:
        break
    lines[last_leaf] = lines[last_leaf].replace("o", "x")
    part3 += 1

print("Part1", part1)
print("Part2", part2)
print("Part3", part3)
