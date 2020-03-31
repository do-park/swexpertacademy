def f(n, k ,c):
    global maxV
    if maxV == N:
        return
    if maxV < c + 1:
        maxV = c + 1
    visited[n] = 1
    for i in range(1, k + 1):
        if adj[n][i] == 1 and visited[i] == 0:
            f(i, k, c + 1)
    visited[n] = 0


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    adj = [[0] * (N + 1) for _ in range(N + 1)]
    visited = [0] * (N + 1)
    maxV = 0
    for m in range(M):
        n1, n2 = map(int, input().split())
        adj[n1][n2] = 1
        adj[n2][n1] = 1
    for i in range(1, N + 1):
        f(i, N, 0)
    print(f'#{tc} {maxV}')