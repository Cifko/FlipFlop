# type:ignore

from functools import lru_cache


def parse_cell(cell):
    try:
        return int(cell)
    except Exception:
        return cell


def parse_line(line: str):
    line = line.split()
    if len(line) == 1:
        line = line[0].split(",")
    if len(line) == 1:
        return parse_cell(line[0])
    return list(map(parse_cell, line))


lines = open("08.txt").readlines()
lines = [line.strip().replace(" ", "") for line in lines]

rules1 = {}
rules2 = {}
for y, line in enumerate(lines):
    if line[0] not in rules1:
        rules1[line[0]] = line[1:]
    rules2[line[:2]] = line[2:]
    rules2[line[1::-1]] = line[2:]


@lru_cache(maxsize=26 * 8)
def get_len1(n, stoat):
    if n == 0:
        return 1
    res = 0
    for c in rules1[stoat]:
        res += get_len1(n - 1, c)
    return res


@lru_cache(maxsize=26 * 26 * 22)
def get_len2(n, pair):
    if n == 0:
        return 2
    res = 0
    l = pair[0]
    for c in rules2[pair]:
        res += get_len2(n - 1, l + c) - 1
        l = c
    res += get_len2(n - 1, l + pair[1])
    return res


part1 = get_len1(7, "A") + get_len1(7, "B")
part2 = get_len2(7, "AB")
part3 = get_len2(21, "AB")

print("Part1", part1)
print("Part2", part2)
print("Part3", part3)
