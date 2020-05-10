# SWEA 1249 보급로

from collections import deque

for tc in range(1, int(input()) + 1):
    N = int(input())
    maps = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    Q = deque()
    Q.append([0, 0])
    visited[0][0] = 1
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    while Q:
        y, x = Q.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < N and 0 <= nx < N and (visited[ny][nx] == 0 or visited[ny][nx] > visited[y][x] + maps[ny][nx]):
                Q.append([ny, nx])
                visited[ny][nx] = visited[y][x] + maps[ny][nx]
    print(f'#{tc} {visited[N - 1][N - 1] - 1}')