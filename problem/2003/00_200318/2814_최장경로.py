from collections import deque

def dfs(index, cnt):
    global result
    if result < cnt:
        result = cnt
    for j in range(N + 1):
        if arr[index][j] == 1 and not visited[j]:
            visited[j] = True
            dfs(j, cnt + 1)
            visited[j] = False

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [[0] * (N + 1) for _ in range(N + 1)]
    Q = deque()
    visited = [False] * (N + 1)
    for m in range(M):
        x, y = map(int, input().split())
        arr[x][y] = 1
        arr[y][x] = 1
    result = 1
    for i in range(1, N + 1):
        visited[i] = True
        dfs(i, 1)
        visited[i] = False
    print(f'#{tc} {result}')