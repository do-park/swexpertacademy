# SWEA 1251 하나로

def find_set(x):
    if parent[x] < 0:
        return x
    parent[x] = find_set(parent[x])
    return parent[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return
    if x < y:
        parent[x] += parent[y]
        parent[y] = x
    else:
        parent[y] += parent[x]
        parent[x] = y
    return

def kruskal():
    result = 0
    count = 0
    for e in range(len(edge)):
        w, x, y = edge[e]
        if find_set(x) == find_set(y):
            continue
        result += w ** 2
        union(x, y)
        count += 1
        if count == N - 1:
            break
    return result

for tc in range(1, int(input()) + 1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    edge = []
    for i in range(N - 1):
        for j in range(i + 1, N):
            x = (X[i] - X[j]) ** 2
            y = (Y[i] - Y[j]) ** 2
            w = (x + y) ** 0.5
            edge.append([w, i, j])
    edge.sort(key = lambda x: x[0])
    parent = [-1] * N
    print(f'#{tc} {(int((kruskal() * E) + 0.5))}')