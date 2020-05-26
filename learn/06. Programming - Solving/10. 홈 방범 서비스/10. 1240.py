# SWEA 1240 단순 2진 암호코드

code = [[[[-1] * 5 for _ in range(5)] for _ in range(5)] for _ in range(5)]
code[3][2][1][1] = 0
code[2][2][2][1] = 1
code[2][1][2][2] = 2
code[1][4][1][1] = 3
code[1][1][3][2] = 4
code[1][2][3][1] = 5
code[1][1][1][4] = 6
code[1][3][1][2] = 7
code[1][2][1][3] = 8
code[3][1][1][2] = 9

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    maps = [list(map(int, input())) for _ in range(N)]
    password = []
    flag = 0
    for n in range(N):
        for m in range(M - 1, -1, -1):
            if maps[n][m]:
                password = maps[n][m - 55 : m + 1]
                flag = 1
                break
        if flag: break
    result = []
    for i in range(8):
        now = 0
        count = 0
        temp = []
        for j in range(7):
            if password[(i * 7) + j] == now:
                count += 1
            else:
                temp.append(count)
                now = password[(i * 7) + j]
                count = 1
        else:
            temp.append(count)
            result.append(code[temp[0]][temp[1]][temp[2]][temp[3]])
    if (((result[0] + result[2] + result[4] + result[6]) * 2 + sum(result)) % 10) == 0:
        print(f'#{tc} {sum(result)}')
    else:
        print(f'#{tc} 0')