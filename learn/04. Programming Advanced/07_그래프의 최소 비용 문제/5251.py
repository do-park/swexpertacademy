# SWEA 5251 최소 이동 거리

from heapq import heappush, heappop
INF = 1e9

def dijkstra():
    dist = [INF] * (N + 1)
    dist[0] = 0
    q = []
    heappush(q, [0, 0])
    while q:
        cost, pos = heappop(q)
        for p, c in route[pos]:
            c += cost
            if c < dist[p]:
                dist[p] = c
                heappush(q, [c, p])
    return dist[N]


for tc in range(1, int(input()) + 1):
    N, E = map(int, input().split())
    route = [[] for _ in range(N + 1)]
    for e in range(E):
        s, e, w = map(int, input().split())
        route[s].append([e, w])
    print(f'#{tc} {dijkstra()}')