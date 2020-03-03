def percent(a):
    return int(a)/100

def dfs(depth, prob):
    global result
    if prob <= result:
        return
    if depth == N:
        result = max(result, prob)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, prob * maps[depth][i])
            visited[i] = False

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maps = [list(map(percent, input().split())) for _ in range(N)]
    visited = [False] * N
    result = 0
    dfs(0, 1)
    print('#{} {:.6f}'.format(tc, result * 100))