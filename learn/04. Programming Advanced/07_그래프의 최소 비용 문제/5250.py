# SWEA 5250 최소 비용

from collections import deque

for tc in range(1, int(input()) + 1):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    q = deque()
    visited[0][0] = 1
    q.append([0, 0, maps[0][0]])
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    while q:
        y, x, h = q.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < N and 0 <= nx < N and (not visited[ny][nx] or (visited[y][x] + 1 + max(maps[ny][nx] - h, 0)) < visited[ny][nx]):
                visited[ny][nx] = visited[y][x] + 1 + max(maps[ny][nx] - h, 0)
                q.append([ny, nx, maps[ny][nx]])
    print(f'#{tc} {visited[N - 1][N - 1] - 1}')