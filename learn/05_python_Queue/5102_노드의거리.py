from collections import deque

for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    maps = [[0] * (V + 1) for _ in range(V + 1)]
    visited = [0] * (V + 1)
    for e in range(E):
        v1, v2 = map(int, input().split())
        maps[v1][v2] = maps[v2][v1] = 1
    S, G = map(int, input().split())
    Q = deque()
    Q.append(S)
    visited[S] = 1
    result = 0
    while Q:
        now = Q.popleft()
        if now == G:
            result = visited[G] - 1
            break
        for i in range(1, V + 1):
            if maps[now][i] and not visited[i]:
                Q.append(i)
                visited[i] = visited[now] + 1
    print(f'#{tc} {result}')