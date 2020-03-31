from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(y, x, cnt, k):
    global result
    if result < cnt + 1:
        result = cnt + 1
    visited[y][x] = 1
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
            if mt[ny][nx] < mt[y][x]:
                dfs(ny, nx, cnt + 1, k)
            elif k and mt[ny][nx] - k < mt[y][x]:
                temp = mt[ny][nx]
                mt[ny][nx] = mt[y][x] - 1
                dfs(ny, nx, cnt + 1, 0)
                mt[ny][nx] = temp
    visited[y][x] = 0


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    mt = []
    maxV = 0
    for n in range(N):
        temp = list(map(int, input().split()))
        mt.append(temp)
        for i in range(N):
            if temp[i] > maxV:
                maxV = temp[i]
                Q = deque()
                Q.append([n, i])
            elif temp[i] == maxV:
                Q.append([n, i])
    result = 0
    visited = [[0] * N for _ in range(N)]
    while Q:
        y, x = Q.popleft()
        dfs(y, x, 0, K)
    print(f'#{tc} {result}')