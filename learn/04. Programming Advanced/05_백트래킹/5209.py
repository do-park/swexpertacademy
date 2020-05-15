# SWEA 5209 최소 생산 비용

def dfs(now, result):
    global answer
    if now == N:
        answer = min(answer, result)
        return
    if answer < result:
        return
    for n in range(N):
        if not visited[n]:
            visited[n] = True
            dfs(now + 1, result + maps[now][n])
            visited[n] = False

for tc in range(1, int(input()) + 1):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    answer = 1500
    dfs(0, 0)
    print(f'#{tc} {answer}')