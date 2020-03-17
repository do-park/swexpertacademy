def dfs(cnt, height):
    if cnt == N:
        if height >= B:
            ans.append(height)
        return
    dfs(cnt + 1, height + clerk[cnt])
    dfs(cnt + 1, height)


T = int(input())

for tc in range(1, T + 1):
    N, B = map(int, input().split())
    clerk = list(map(int, input().split()))
    ans = []
    dfs(0, 0)
    print(f'#{tc} {min(ans) - B}')