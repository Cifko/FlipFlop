# type:ignore

from functools import lru_cache

@lru_cache
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


lines = open("02.txt").readlines()
line = lines[0]
h1 = h2 = h3 = 0
i = 0
up = True
part1 = part2 = part3 = 0
for c in line:
    if c == "v":
        if up:
            h3 += fib(i)
            part3 = max(part3, h3)
            i = 0
        i += 1
        h1 -= 1
        h2 -= i
        up = False
    if c == "^":
        if not up:
            h3 -= fib(i)
            i = 0
        i += 1
        h1 += 1
        h2 += i
        up += 1
        part1 = max(part1, h1)
        part2 = max(part2, h2)
        part3 = max(part3, h3)

if up:
    h3 += fib(i)
    part3 = max(part3, h3)

print("Part1", part1)
print("Part2", part2)
print("Part3", part3)
