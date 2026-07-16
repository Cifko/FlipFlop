# type:ignore

from collections import Counter, deque, defaultdict
from math import factorial
from functools import lru_cache
from pyperclip import copy
from downloader import download


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


lines = download(11)
lines = [parse_line(line) for line in lines]

res = 0


def tree(dna, i, sunlight, stems, fixed_sprouts):
    sprouts = {(i * 10, 1): 0}
    # stems = {}
    for age in range(1, 100 + 1):
        new_sprouts = defaultdict(int)
        for sprout in sprouts:
            x, y = sprout
            stems[sprout] = sprouts[sprout]
            sunlight[x].append(y)
            left, up, right = dna[sprouts[sprout]]
            for nx, ny, r in [(x - 1, y, left), (x, y + 1, up), (x + 1, y, right)]:
                if r != "XX":
                    if (nx, ny) not in stems and (nx, ny) not in fixed_sprouts:
                        new_sprouts[(nx, ny)] = max(r, new_sprouts[(nx, ny)])
        sprouts = new_sprouts
        for x in sunlight[x]:
            sunlight[x] = sorted(sunlight[x], reverse=True)

        my = mxl = mxr = 0
        for x, y in sprouts:
            mxl = min(mxl, x)
            mxr = max(mxr, x)
            my = max(my, y)

        for x, y in stems:
            mxl = min(mxl, x)
            mxr = max(mxr, x)
            my = max(my, y)

        for y in range(1, my + 1)[::-1]:
            for x in range(mxl, mxr + 1):
                if (x, y) in sprouts:
                    print("@", end="")
                elif (x, y) in stems:
                    print("#", end="")
                else:
                    print(" ", end="")
            print()

        energy = 0
        # print("stems", len(stems), len(sprouts), sprouts)
        for x, y in stems:
            above = sunlight[x].index(y)
            # if y == 1:
            # print(x, above)
            energy += max(0, 3 - above) * min(10, y)
        if energy < 3 * (len(stems) + len(sprouts)) and age >= 5:
            break
    for sprout in sprouts:
        fixed_sprouts[sprout] = sprouts[sprout]
    print("tree", i, age, energy, len(stems) + len(sprouts))
    return len(stems) + len(sprouts), stems, fixed_sprouts


def trees(dnas, sprouts):
    l = len(dnas)

    stems = {}
    sunlight = defaultdict(list)
    died = set()
    fixed_sprouts = set()
    for age in range(1, 101):
        new_sprouts = defaultdict(lambda: (-1, -1))
        for t in range(l)[::-1]:
            for sprout in sprouts:
                x, y = sprout
                tt, dna_index = sprouts[sprout]
                if tt != t:
                    continue
                if t in died:
                    new_sprouts[sprout] = sprouts[sprout]
                    continue
                stems[sprout] = sprouts[sprout]
                sunlight[x].append(y)
        for t in range(l)[::-1]:
            for sprout in sprouts:
                tt, dna_index = sprouts[sprout]
                if tt != t:
                    continue
                if t in died:
                    new_sprouts[sprout] = sprouts[sprout]
                    continue
                x, y = sprout
                left, up, right = dnas[t][dna_index]
                for nx, ny, r in [(x - 1, y, left), (x, y + 1, up), (x + 1, y, right)]:
                    if type(r) is int:
                        if (nx, ny) not in stems and (nx, ny) not in fixed_sprouts:
                            new_sprouts[(nx, ny)] = max((t, r), new_sprouts[(nx, ny)])
        sprouts = new_sprouts

        if len(set(sprouts.keys()) & set(stems)) > 0:
            print("WTF", set(sprouts.keys()) & set(stems))
        for t in range(l):
            for x in sunlight:
                sunlight[x] = sorted(sunlight[x], reverse=True)

            # print(t, age, energy, 3 * required)
            if t not in died:
                required = energy = 0
                for sprout in new_sprouts:
                    if new_sprouts[sprout][0] == t:
                        required += 1
                for x, y in stems:
                    if stems[(x, y)][0] == t:
                        required += 1
                        above = sunlight[x].index(y)
                        energy += max(0, 3 - above) * min(10, y)
                if energy < 3 * required and age >= 5:
                    for sprout in sprouts:
                        if sprouts[sprout][0] == t:
                            fixed_sprouts.add(sprout)
                            x, y = sprout
                            # sunlight[x].append(y)
                    # print("die", len(dnas) - t, age, energy, 3 * required)
                    died.add(t)
    return len(stems) + len(sprouts), sprouts


part1 = part2 = part3 = 0

dnas = []
stems = {}
sprouts = {}
sunlight = defaultdict(list)

part1 = 0
for t in range(0, len(lines), 3):
    dna = {}
    for x in range(len(lines[t])):
        up = lines[t][x]
        left = lines[t + 1][x * 3]
        right = lines[t + 1][x * 3 + 2]
        rule = lines[t + 1][x * 3 + 1]
        dna[rule] = (left, up, right)
    dnas += [dna]
    part1 += trees([dna], {(0, 1): (0, 0)})[0]

dnas = dnas[::-1]
sprouts = {(-x * 10, 1): (x, 0) for x in range(len(dnas))}
part2, sprouts = trees(dnas, sprouts)

for _ in range(2):
    seeds = {}
    for s in sprouts:
        x, y = s
        if x not in seeds:
            seeds[x] = (y, sprouts[s][0])
        else:
            seeds[x] = max(seeds[x], (y, sprouts[s][0]))
    # print("cmp", len(sprouts), len(seeds))
    order = sorted(seeds.keys(), reverse=True)
    new_dnas = []
    sprouts = {}
    for i, o in enumerate(order):
        sprouts[(o, 1)] = (i, 0)
        new_dnas.append(dnas[seeds[o][1]])
    dnas = new_dnas
    part3, sprouts = trees(dnas, sprouts)

print("Part1", part1)
print("Part2", part2)
print("Part3", part3)
