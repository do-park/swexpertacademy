# SWEA 2117 홈 방범 서비스

cost = [i * i + (i - 1) * (i - 1) for i in range(22)]
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    home = []
    for i in range(N):
        for j in range(N):
            if maps[i][j]:
                home.append((i, j))
    result = 0
    for i in range(N):
        for j in range(N):
            cnt = [0] * (N + 2)
            for p, q in home:
                dist = abs(i - p) + abs(j - q) + 1
                if dist <= N + 1:
                    cnt[dist] += 1
            for k in range(1, N + 2):
                cnt[k] += cnt[k - 1]
                if cnt[k] * M >= cost[k]:
                    if result < cnt[k]:
                        result = cnt[k]
    print(f'#{tc} {result}')