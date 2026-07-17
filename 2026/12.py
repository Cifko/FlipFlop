# type:ignore

from downloader import download
from itertools import product, combinations, chain


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


lines = download(12)
lines = [parse_line(line) for line in lines]

i = lines.index([])
call = list(chain.from_iterable(lines[:i]))
data = list(chain.from_iterable(lines[i + 1 :]))


def is_bingo_nd(n):
    res = []

    for i in range(1, n + 1):
        for v in product([0, 4], repeat=i):
            for vi in combinations(range(n), i):
                p = [0] * n
                ji = set(range(n))
                for c, d in zip(v, vi):
                    p[d] = c
                    ji.remove(d)
                for w in range(3 ** (n - i)):
                    for d in ji:
                        p[d] = w % 3 + 1
                        w //= 3
                    u = 0
                    for k in p:
                        u *= 5
                        u += k
                    ds = []
                    for j in p:
                        if j == 0:
                            ds.append([0, 1])
                        elif j == 4:
                            ds.append([-1, 0])
                        else:
                            ds.append([0])
                    for d in product(*ds):
                        delta = 0
                        for j in d:
                            delta *= 5
                            delta += j
                            if delta < 0:
                                break
                        if delta > 0:
                            res.append([u + j * delta for j in range(5)])
    return res


for d in range(2, 5):
    pos = is_bingo_nd(d)
    res = 0
    nums = set()
    res = 0
    for n in call:
        nums.add(n)
        if (
            res == 0
            and sum(
                all(data[x + u] in nums for x in p)
                for p in pos
                for u in range(0, len(data), 5**d)
            )
            >= 5
        ):
            res = n
            print(f"part{d - 1}", res)
