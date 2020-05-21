# SWEA 5248 그룹 나누기

def find_set(x):
    if parent[x] < 0:
        return x
    else:
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


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    E = list(map(int, input().split()))
    parent = [0] + [-1] * N
    for m in range(0, M * 2, 2):
        union(E[m], E[m + 1])
    count = 0
    for n in range(N + 1):
        if parent[n] < 0:
            count += 1
    print(f'#{tc} {count}')
