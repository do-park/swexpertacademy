# SWEA 1249 보급로

from collections import deque

INF = 1e9
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for tc in range(1, int(input()) + 1):
    N = int(input())
    maps = [list(map(int, input())) for _ in range(N)]
    visited = [[INF] * N for _ in range(N)]
    q = deque()
    visited[0][0] = maps[0][0]
    q.append([0, 0])
    while q:
        y, x = q.popleft()
        cost = visited[y][x]
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] > cost + maps[ny][nx]:
                visited[ny][nx] = cost + maps[ny][nx]
                q.append([ny, nx])
    print(f'#{tc} {visited[N- 1][N - 1]}')