# SWEA 1248 공통조상

def findRoot(x, root):
    if parent[x] == 1:
        root.append(1)
        return
    root.append(parent[x])
    findRoot(parent[x], root)

def findChild(x):
    global result2
    if child[x]:
        result2 += len(child[x])
        for i in child[x]:
            findChild(i)
    else:
        return

for tc in range(1, int(input()) + 1):
    V, E, A, B = map(int, input().split())
    edges = list(map(int, input().split()))
    parent = [-1] * (V + 1)
    child = [[] for _ in range(V + 1)]
    for e in range(0, len(edges), 2):
        parent[edges[e + 1]] = edges[e]
        child[edges[e]].append(edges[e + 1])
    rootA = [A]
    rootB = [B]
    findRoot(A, rootA)
    findRoot(B, rootB)
    rootA = rootA[::-1]
    rootB = rootB[::-1]
    result1, result2 = 0, 1
    for i in range(len(rootA)):
        if rootA[i] != rootB[i]:
            result1 = rootA[i - 1]
            break
    findChild(result1)
    print(f'#{tc} {result1} {result2}')