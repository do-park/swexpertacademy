def perc(num):
    return int(num) / 100

def f(n, k, res):
    global result
    if result >= res:
        return
    if n == k:
        if result < res:
            result = res
    else:
        for i in range(k):
            if used[i] == 0:
                used[i] = 1
                f(n + 1, k, res * maps[i][n])
                used[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maps = [list(map(perc, input().split())) for _ in range(N)]
    used = [False] * N
    p = [0] * N
    result = 0
    f(0, N, 1)
    result *= 100
    print('#{} {:.6f}'.format(tc, result))