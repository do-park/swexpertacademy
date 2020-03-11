T = int(input())

for tc in range(1, T + 1):
    flag = 1
    arr = [list(map(int, input().split())) for _ in range(9)]

    for i in range(9):
        check = [0] * 10
        for j in range(9):
            check[arr[i][j]] += 1
            if check[arr[i][j]] > 1:
                flag = 0

    if flag:
        for j in range(9):
            check = [0] * 10
            for i in range(9):
                check[arr[i][j]] += 1
                if check[arr[i][j]] > 1:
                    flag = 0

    if flag:
        start = [[0, 0], [3, 0], [6, 0], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]
        while start:
            y, x = start.pop()
            isused = [0] * 10
            for i in range(3):
                for j in range(3):
                    isused[arr[i][j]] += 1
                    if isused[arr[i][j]] > 1:
                        flag = 0

    print(f'#{tc} {flag}')