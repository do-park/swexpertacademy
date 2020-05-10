#  SWEA 1954 달팽이 숫자

for tc in range(1, int(input()) + 1):
    N = int(input())
    snail = [[0] * N for _ in range(N)]
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    x, y, d = 0, 0, 0
    s = 1
    end = N * N
    while s <= end:
        snail[y][x] = s
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 <= ny < N and 0 <= nx < N and not snail[ny][nx]:
            y, x = ny, nx
        else:
            d = (d + 1) % 4
            y = y + dy[d]
            x = x + dx[d]
        s += 1
    print(f'#{tc}')
    for i in range(N):
        print(*snail[i])