# SWEA 1486 장훈이의 높은 선반

def dfs(k=0, res=0):
    if res >= B or k == N:
        global result
        if B <= res < result:
            result = res
        return
    dfs(k + 1, res + H[k])
    dfs(k + 1, res)

for tc in range(1, int(input()) + 1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    result = 1e9
    dfs()
    print(f'#{tc} {result - B}')