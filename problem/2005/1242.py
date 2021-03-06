P = {(2, 1, 1): 0, (2, 2, 1): 1, (1, 2, 2): 2, (4, 1, 1): 3, (1, 3, 2): 4, (2, 3, 1): 5, (1, 1, 4): 6, (3, 1, 2): 7,
     (2, 1, 3): 8, (1, 1, 2): 9}
hexTobin = {'0': [0, 0, 0, 0], '1': [0, 0, 0, 1], '2': [0, 0, 1, 0], '3': [0, 0, 1, 1],
            '4': [0, 1, 0, 0], '5': [0, 1, 0, 1], '6': [0, 1, 1, 0], '7': [0, 1, 1, 1],
            '8': [1, 0, 0, 0], '9': [1, 0, 0, 1], 'A': [1, 0, 1, 0], 'B': [1, 0, 1, 1],
            'C': [1, 1, 0, 0], 'D': [1, 1, 0, 1], 'E': [1, 1, 1, 0], 'F': [1, 1, 1, 1]}

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [[] for _ in range(N)]
    for i in range(N):
        tmp = input()
        for j in range(M):
            arr[i] += hexTobin[tmp[j]]


    def find():
        ans = 0
        for i in range(N):
            j = M * 4 - 1
            while j >= 55:
                if arr[i][j] and arr[i - 1][j] == 0:
                    pwd = []
                    for _ in range(8):
                        c2 = c3 = c4 = 0
                        while arr[i][j] == 0: j -= 1
                        while arr[i][j] == 1: c4, j = c4 + 1, j - 1
                        while arr[i][j] == 0: c3, j = c3 + 1, j - 1
                        while arr[i][j] == 1: c2, j = c2 + 1, j - 1
                        MIN = min(c2, c3, c4)
                        pwd.append(P[(c2 // MIN, c3 // MIN, c4 // MIN)])

                    b = pwd[0] + pwd[2] + pwd[4] + pwd[6]
                    a = pwd[1] + pwd[3] + pwd[5] + pwd[7]
                    if (a * 3 + b) % 10 == 0:
                        ans += a + b
                j -= 1
        return ans


    print('#{} {}'.format(tc, find()))