# 2
# 2 2 4 4 1  ( [2,2] 부터 [4,4] 까지 color 1 (빨강) 으로 칠한다 )
# 3 3 6 6 2 ( [3,3] 부터 [6,6] 까지 color 2 (파랑) 으로 칠한다 )


T = int(input())

for tc in range(0, T):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]
    results = [0] * 100

    for x in range(0, N):
        for i in range(area[x][0], area[x][2] + 1):
            for j in range(area[x][1], area[x][3] + 1):
                results[10 * j + i] += area[x][4]

    print('#{} {}'.format(tc + 1, results.count(3)))