from collections import deque

for tc in range(1, int(input()) + 1):
    E, N = map(int, input().split())
    vertex = [[0, 0, 0] for _ in range(E + 2)] # L, R, P
    nodes = list(map(int, input().split()))
    for i in range(0, len(nodes), 2):
        if vertex[nodes[i]][0]:
            vertex[nodes[i]][1] = nodes[i + 1]
        else:
            vertex[nodes[i]][0] = nodes[i + 1]
        vertex[nodes[i + 1]][2] = nodes[i]
    count = 1
    Q = deque()
    Q.append(N)
    while Q:
        x = Q.popleft()
        if vertex[x][0]:
            Q.append(vertex[x][0])
            count += 1
        if vertex[x][1]:
            Q.append(vertex[x][1])
            count += 1
    print(f'#{tc} {count}')