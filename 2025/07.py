# type:ignore
from math import factorial

lines = [l.strip() for l in open("07.txt").readlines()]

part1 = part2 = part3 = 0

for line in lines:
    x, y = map(int, line.split())
    part1 += factorial(x + y - 2) // factorial(x - 1) // factorial(y - 1)
    part2 += (
        factorial(x + y + x - 3)
        // factorial(x - 1)
        // factorial(y - 1)
        // factorial(x - 1)
    )
    k = factorial((y - 1) * x)
    for _ in range(x):
        k //= factorial(y - 1)
    part3 += k

print("Part1", part1)
print("Part2", part2)
print("Part3", part3)
