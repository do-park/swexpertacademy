# SWEA 1954 달팽이 숫자

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

for tc in range(1, int(input()) + 1):
    N = int(input())
    maps = [[0] * N for _ in range(N)]
    d = 0
    y, x = 0, 0
    maps[y][x] = 1
    n = 2
    while n <= N ** 2:
        ny, nx = y + dy[d], x + dx[d]
        if 0 <= ny < N and 0 <= nx < N and not maps[ny][nx]:
            maps[y + dy[d]][x + dx[d]] = n
            n += 1
            y, x = ny, nx
        else:
            d = (d + 1) % 4
    print(f'#{tc}')
    for i in range(N):
        print(*maps[i])