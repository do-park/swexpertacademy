T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]
    lst = [0] * (N * N + 1)

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    for i in range(N):
        for j in range(N):
            for d in range(4):
                y = i + dy[d]
                x = j + dx[d]
                if 0 <= x < N and 0 <= y < N and maps[y][x] == maps[i][j] + 1:
                    lst[maps[i][j]] = 1
    result_s = 0
    result = 0
    cnt = 0
    for i in range(N * N, -1, -1):
        if lst[i]:
            cnt += 1
        else:
            if cnt >= result:
                result_s = i + 1
                result = cnt
            cnt = 0
    print(f'#{tc} {result_s} {result + 1}')