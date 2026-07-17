# type:ignore

import heapq

lines = open("09.txt").readlines()


def solve(part: int):
    # Moves, no teleport, x, y
    s = [(0, True, 1, 1)]

    visited = set()
    while s:
        m, no_teleport, x, y = heapq.heappop(s)
        if lines[y][x] == "E":
            return m
        if (x, y) in visited:
            continue
        visited.add((x, y))

        for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if lines[ny][nx] in ".E":
                heapq.heappush(s, (m + 1, True, nx, ny))
            if part > 1:
                dx = nx - x
                dy = ny - y
                i = 0
                while True:
                    i += 1
                    nx = dx * i + x
                    ny = dy * i + y
                    if lines[ny][nx] == "#":
                        i -= 1
                        break
                nx = dx * i + x
                ny = dy * i + y
                if part == 2:
                    heapq.heappush(s, (m + 1, True, nx, ny))
                else:
                    extra = 0
                    if (
                        lines[y][x - 1]
                        == lines[y][x + 1]
                        == lines[y - 1][x]
                        == lines[y + 1][x]
                        == "."
                    ):
                        extra += 1
                    heapq.heappush(s, (m + extra + 2 + (no_teleport), not True, nx, ny))


part1 = solve(1)
part2 = solve(2)
part3 = solve(3)

print("Part1", part1)
print("Part2", part2)
print("Part3", part3)
