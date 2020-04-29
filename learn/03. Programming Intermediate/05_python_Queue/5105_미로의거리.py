from collections import deque

for tc in range(1, int(input()) + 1):
    N = int(input())
    maps = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    Q = deque()
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 2:
                Q.append([i, j])
                visited[i][j] = 1
                break
        if Q:
            break
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    result = 0
    while Q:
        y, x = Q.popleft()
        if maps[y][x] == 3:
            result = visited[y][x] - 2
            break
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < N and 0 <= nx < N and maps[ny][nx] != 1 and not visited[ny][nx]:
                Q.append([ny, nx])
                visited[ny][nx] = visited[y][x] + 1
    print(f'#{tc} {result}')