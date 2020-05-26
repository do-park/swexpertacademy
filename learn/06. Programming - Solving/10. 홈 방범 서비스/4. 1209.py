# SWEA 1209 Sum

for tc in range(1, 11):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(100)]
    result = -1
    # 가로
    for i in range(100):
        if sum(maps[i]) > result:
            result = sum(maps[i])
    # 세로
    for j in range(100):
        temp = 0
        for i in range(100):
            temp += maps[i][j]
        if temp > result:
            result = temp
    # 대각선
    temp1 = 0
    temp2 = 0
    for i in range(100):
        temp1 += maps[i][i]
        temp2 += maps[i][99 - i]
    result = max(result, temp1, temp2)
    print(f'#{tc} {result}')