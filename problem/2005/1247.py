# SWEA 1247 최적 경로

def DFS(now, temp=0, n=0):
    global result
    if temp >= result:
        return
    if N == n:
        x = abs(now[0] - en[0])
        y = abs(now[1] - en[1])
        temp += x + y
        result = min(result, temp)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            x = abs(now[0] - V[i][0])
            y = abs(now[1] - V[i][1])
            DFS(V[i], temp + x + y, n + 1)
            visited[i] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    st = [numbers[0], numbers[1]]
    en = [numbers[2], numbers[3]]
    V = []
    for i in range(4, len(numbers), 2):
        V.append([numbers[i], numbers[i + 1]])
    visited = [0] * N
    result = 1e9
    DFS(st)
    print(f'#{tc} {result}')