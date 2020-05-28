# SWEA 1247 최적 경로

def DFS(now, temp=0, n=0):
    global result
    if temp >= result:
        return
    if N == n:
        temp += adj[now][1]
        result = min(result, temp)
        return
    for i in range(2, N + 2):
        if not visited[i]:
            visited[i] = 1
            DFS(i, temp + adj[now][i], n + 1)
            visited[i] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    V = []
    for i in range(0, len(numbers), 2):
        V.append([numbers[i], numbers[i + 1]])
    visited = [0] * (N + 2)
    adj = [[0] * (N + 2) for _ in range(N + 2)]
    for i in range(N + 2):
        for j in range(i + 1, N + 2):
            adj[i][j] = adj[j][i] = abs(V[i][0] - V[j][0]) + abs(V[i][1] - V[j][1])
    result = 1e9
    DFS(0)
    print(f'#{tc} {result}')