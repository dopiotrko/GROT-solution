sample = [
    ['u', 'd', 'u', 'u'], # ↑ ↓ ↑ ↑
    ['u', 'r', 'l', 'l'], # ↑ → ← ←
    ['u', 'u', 'l', 'u'], # ↑ ↑ ← ↑
    ['l', 'd', 'u', 'l'], # ← ↓ ↑ ←
]


class OutOfBoardException(ValueError):
    pass


def move(x, y):
    if sample[x][y] == 'u':
        x -= 1
    elif sample[x][y] == 'd':
        x += 1
    elif sample[x][y] == 'r':
        y += 1
    else:
        y -= 1
    if x > 3 or x < 0 or y > 3 or y < 0:
        raise OutOfBoardException
    return x, y


paths = []
for start_x in range(4):
    for start_y in range(4):
        x, y = start_x, start_y
        path = []
        while [x, y] not in path:
            path.append([x, y])
            try:
                x, y = move(x, y)
            except OutOfBoardException:
                break
        paths.append(path)

lengths = [len(s_path) for s_path in paths]
print(paths[lengths.index(max(lengths))][0])
