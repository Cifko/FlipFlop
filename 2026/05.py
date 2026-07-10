# type:ignore

lines = open("05.txt").readlines()
lines = [list(line.strip()) for line in lines]


def find_loop(part3=False):
    x = y = 0
    visited = set()
    repeated_visit = 0
    while True:
        is_visited = (x, y) in visited
        if is_visited:
            repeated_visit += 1
            if repeated_visit == [1, 4][part3]:
                break
        visited.add((x, y))
        if is_visited and 0 < x < len(lines[0]) - 1 and 0 < y < len(lines) - 1:
            match lines[y][x]:
                case "v":
                    x -= 1
                case "^":
                    x += 1
                case ">":
                    y += 1
                case "<":
                    y -= 1
        else:
            match lines[y][x]:
                case "v":
                    y += 1
                case "^":
                    y -= 1
                case ">":
                    x += 1
                case "<":
                    x -= 1
    return len(visited)


part1 = find_loop()
part2 = part3 = 0

for y in range(1, len(lines) - 1):
    for x in range(1, len(lines[0]) - 1):
        for d in "v^<>":
            old = lines[y][x]
            lines[y][x] = d
            part2 = max(part2, find_loop())
            part3 = max(part3, find_loop(True))
            lines[y][x] = old

print("Part1", part1)
print("Part2", part2)
print("Part3", part3)
