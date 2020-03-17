def dfs(temp, cnt, a, s, m, d):
    if cnt == N:
        result.append(temp)

    if a:
        dfs(temp + num[cnt], cnt + 1, a - 1, s, m, d)
    if s:
        dfs(temp - num[cnt], cnt + 1, a, s - 1, m, d)
    if m:
        dfs(temp * num[cnt], cnt + 1, a, s, m - 1, d)
    if d:
        dfs(int(temp / num[cnt]), cnt + 1, a, s, m, d - 1)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    oper = list(map(int, input().split()))
    num = list(map(int, input().split()))
    result = []
    dfs(num[0], 1, *oper)
    print(f'#{tc} {max(result) - min(result)}')