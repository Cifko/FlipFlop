# type:ignore

lines = open("07.txt").readlines()

instructions = lines[0].strip()
sushi = [tuple(map(int, line.split(","))) for line in lines[2:]]

x = y = 0
snake = [(x, y)]
eat_itself = 0
sushi_index = 0
part1 = part2 = part3 = 0

for i, c in enumerate(instructions):
    match c:
        case "v":
            y -= 1
        case "^":
            y += 1
        case "<":
            x -= 1
        case ">":
            x += 1
    if i == len(instructions) // 2:
        part1 = sushi_index
    for j, s in enumerate(snake):
        # This is weird, because if he moves onto the very end of the tail it's fine, but if moves onto a middle tile, that tile doesn't survive
        if s == (x, y) and j > 0:
            if eat_itself == 0:
                part2 = len(snake)
            snake = snake[j + 1 :]
            eat_itself += 1
    if sushi_index < len(sushi) and (x, y) == sushi[sushi_index]:
        sushi_index += 1
        snake.append((x, y))
    else:
        snake = snake[1:] + [(x, y)]

part3 = len(snake) * eat_itself

print("Part1", part1)
print("Part2", part2)
print("Part3", part3)
