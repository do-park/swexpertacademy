def dfs(root):
    if vertex[root][2]:
        return vertex[root][2]
    else:
        vertex[root][2] = dfs(vertex[root][0])
        if vertex[root][1] <= N:
            vertex[root][2] += dfs(vertex[root][1])
        return vertex[root][2]

for tc in range(1, int(input()) + 1):
    N, M, L = map(int, input().split())
    vertex = [[0, 0, 0] for _ in range(N + 1)] # L, R, result
    for i in range(1, N + 1):
        vertex[i][0] = i * 2
        vertex[i][1] = i * 2 + 1
    for m in range(M):
        i, x = map(int, input().split())
        vertex[i][2] = x
    print(f'#{tc} {dfs(L)}')