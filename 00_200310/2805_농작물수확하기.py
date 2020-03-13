for tc in range(1, int(input()) + 1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    result = 0
    n = N // 2
    for i in range(n):
        for j in range(n - i, n + i + 1):
            result += farm[i][j]
    for i in range(n, -1, -1):
        for j in range(n - i, n + i + 1):
            result += farm[N - i - 1][j]
    print(f'#{tc} {result}')