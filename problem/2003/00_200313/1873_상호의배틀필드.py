T = int(input())
for tc in range(1, T + 1):
    H, W = map(int, input().split())
    field = []
    d, y, x = 0, 0, 0
    for h in range(H):
        temp = list(map(str, input()))
        for w in range(W):
            if temp[w] == '^':
                d = 'U'
                y, x = h, w
                temp[w] = '.'
            elif temp[w] == 'v':
                d = 'D'
                y, x = h, w
                temp[w] = '.'
            elif temp[w] == '<':
                d = 'L'
                y, x = h, w
                temp[w] = '.'
            elif temp[w] == '>':
                d = 'R'
                y, x = h, w
                temp[w] = '.'
        field.append(temp)
    N = int(input())
    cmd = list(map(str, input()))
    for n in range(N):
        if cmd[n] == 'L':
            if (x - 1) >= 0 and field[y][x - 1] == '.':
                d = 'L'
                x -= 1
            else:
                d = 'L'
        elif cmd[n] == 'R':
            if (x + 1) < W and field[y][x + 1] == '.':
                d = 'R'
                x += 1
            else:
                d = 'R'
        elif cmd[n] == 'U':
            if (y - 1) >= 0 and field[y - 1][x] == '.':
                d = 'U'
                y -= 1
            else:
                d = 'U'
        elif cmd[n] == 'D':
            if (y + 1) < H and field[y + 1][x] == '.':
                d = 'D'
                y += 1
            else:
                d = 'D'
        elif cmd[n] == 'S':
            if d == 'U':
                i = 1
                while True:
                    if y - i < 0:
                        break
                    if field[y - i][x] == '*':
                        field[y - i][x] = '.'
                        break
                    elif field[y - i][x] == '#':
                        break
                    i += 1
            elif d == 'D':
                i = 1
                while True:
                    if y + i >= H:
                        break
                    if field[y + i][x] == '*':
                        field[y + i][x] = '.'
                        break
                    elif field[y + i][x] == '#':
                        break
                    i += 1
            if d == 'L':
                i = 1
                while True:
                    if x - i < 0:
                        break
                    if field[y][x - i] == '*':
                        field[y][x - i] = '.'
                        break
                    elif field[y][x - i] == '#':
                        break
                    i += 1
            elif d == 'R':
                i = 1
                while True:
                    if x + i >= W:
                        break
                    if field[y][x + i] == '*':
                        field[y][x + i] = '.'
                        break
                    elif field[y][x + i] == '#':
                        break
                    i += 1

    if d == 'U':
        field[y][x] = '^'
    elif d == 'D':
        field[y][x] = 'v'
    elif d == 'L':
        field[y][x] = '<'
    elif d == 'R':
        field[y][x] = '>'
    print(f'#{tc}', end=' ')
    for h in range(H):
        for w in range(W):
            print(field[h][w], end='')
        print()