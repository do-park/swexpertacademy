T = int(input())
for tc in range(1, T + 1):
    N, M= map(int, input().split())
    flag = []
    color = [[0, 0, 0] for _ in range(N)]
    for n in range(N):
        temp = list(map(str, input()))
        flag.append(temp)
        for m in range(M):
            if temp[m] == 'W':
                color[n][0] += 1
            elif temp[m] == 'B':
                color[n][1] += 1
            else:
                color[n][2] += 1
    result = 2501
    for w in range(0, N-2):
        for r in range(N - 1, w, -1):
            res = 0
            for b in range(0, N):
                if b <= w:
                    res += color[b][0]
                elif b >= r:
                    res += color[b][2]
                else:
                    res += color[b][1]
            result = min(result, M * N - res)
    print(f'#{tc} {result}')