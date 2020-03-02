def dfs(temp, cnt):
    if cnt >= 12:
        result.append(temp)
        return

    if plan[cnt] > 0:
        dfs(temp + fee[0] * plan[cnt], cnt + 1)
        dfs(temp + fee[1], cnt + 1)
        dfs(temp + fee[2], cnt + 3)
        dfs(temp + fee[3], cnt + 12)
    else:
        dfs(temp, cnt + 1)


T = int(input())

for tc in range(1, T + 1):
    fee = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    result = []
    dfs(0, 0)
    print(f'#{tc} {min(result)}')