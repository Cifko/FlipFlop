# type:ignore
from string import ascii_lowercase, ascii_uppercase, ascii_letters, digits

chars = ascii_letters + digits
ascii_lowercase = set(ascii_lowercase)
ascii_uppercase = set(ascii_uppercase)
digits = set(digits)


def score1(password: str) -> int:
    l = len(password)
    password = set(password)
    return (
        (len(ascii_uppercase & password) > 0)
        + (len(ascii_lowercase & password) > 0)
        + (len(digits & password) > 0)
    ) * l


def score2(password: str) -> int:
    seven = (digits & set(password)) == {"7"} and 7 or 0
    last = None
    cnt = 0
    sq = 0
    for c in password:
        if c != last:
            cnt = 0
        last = c
        cnt += 1
        sq = max(sq, cnt)
    if sq > 2:
        sq *= sq
    else:
        sq = 0
    score = score1(password) + (seven + sq) * len(password)
    if "red" in password or "green" in password or "blue" in password:
        score *= 3
    return score


lines = [line.strip() for line in open("03.txt").readlines()]

part1 = max(lines, key=score1)
part2 = max(lines, key=score2)
part3 = max(sum(score2(line + c) for line in lines) for c in chars)

print("Part1", part1)
print("Part2", part2)
print("Part3", part3)
