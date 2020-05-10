# SWEA 1210 Ladder1

for tc in range(10):
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    for n in range(100):
        if ladder[99][n] == 2:
            y = 99
            x = n
            break
    dy = [0, 0, -1]
    dx = [-1, 1, 0]
    while y > 0:
        for d in range(3):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < 100 and 0 <= nx < 100 and ladder[ny][nx] == 1:
                y, x = ny, nx
                ladder[y][x] = 2
                break
    print(f'#{N} {x}')