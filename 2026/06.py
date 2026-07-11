# type:ignore


def erasten(N):
    E = [True] * (N + 1)
    P = []
    p = 2
    while p <= N:
        if E[p]:
            P += [p]
            x = p
            while x <= N:
                E[x] = False
                x += p
        p += 1
    return P


lines = open("06.txt").readlines()

primes = erasten(len(lines) * len(lines[0]))

lights = []
bluetooth = {}
for j, line in enumerate(lines):
    for i, cell in enumerate(line):
        match cell:
            case "S":
                x, y = i, j
            case "*":
                lights.append((i, j))
            case c if "a" <= c <= "z" or "A" <= c <= "Z":
                bluetooth[cell] = (i, j)


stack = [(x, y, "L", "", "S")]

on_off = [0] * len(lights)
light_enabled_by = {}

bt_size = {}
enabled_by = {}
visited = set()
while stack:
    x, y, dir, from_bt, current_bt = stack.pop()
    if (x, y) in visited:
        continue
    if current_bt not in bt_size:
        bt_size[current_bt] = 0
    match lines[y][x]:
        case "#" | "3":
            bt_size[current_bt] += 1
        case "*":
            light_enabled_by[(x, y)] = current_bt
            on_off[lights.index((x, y))] = dir
    visited.add((x, y))

    for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if not (0 < nx < len(lines[0]) and 0 < ny < len(lines)):
            continue
        cell = lines[ny][nx]
        match cell:
            case "#" | "*" | "3":
                stack.append((nx, ny, "LR"[dir == "L"], from_bt, current_bt))
            case c if "a" <= c <= "z":
                nx, ny = bluetooth[cell.upper()]
                if cell not in from_bt:
                    enabled_by[cell] = current_bt
                stack.append((nx, ny, "LR"[dir == "R"], current_bt, cell))

turn_off = ""
for x in bt_size:
    if x != "S" and bt_size[x] in primes:
        turn_off += x

while True:
    change = False
    for from_bt in enabled_by:
        if enabled_by[from_bt] in turn_off and from_bt not in turn_off:
            turn_off += from_bt
            change = True
    if not change:
        break

part1 = part2 = part3 = 0
for i, cell in enumerate(on_off):
    x, y = lights[i]
    if cell == 0:
        continue
    if light_enabled_by[(x, y)] == "S":
        part1 *= 2
        part1 += cell == "L"
    part2 *= 2
    part2 += cell == "L"
    if light_enabled_by[(x, y)] not in turn_off:
        part3 *= 2
        part3 += cell == "L"

print("Part1", part1)
print("Part2", part2)
print("Part3", part3)
