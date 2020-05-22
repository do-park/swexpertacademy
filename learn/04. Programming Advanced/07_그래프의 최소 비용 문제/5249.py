# SWEA 5249 최소 신장 트리

from heapq import heappush, heappop
INF = 1e9

def prim():
    dist = [INF] * (v + 1)
    q = []
    heappush(q, [0, 0])
    while q:
        cost, pos = heappop(q)
        if dist[pos] == INF:
            dist[pos] = cost
            for p, c in edge[pos]:
                if dist[p] > c:
                    heappush(q, [c, p])
    return sum(dist)


for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    edge = [[] for _ in range(V + 1)]
    for e in range(E):
        u, v, w = map(int, input().split())
        edge[u].append([v, w])
        edge[v].append([u, w])
    print(f'#{tc} {prim()}')
