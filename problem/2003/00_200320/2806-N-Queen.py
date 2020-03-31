def dfs(x):
    global result

    if x == N:
        result += 1
    else:
        for y in range(N):
            if not (a[y] or b[x + y] or c[x - y + N - 1]):
                a[y] = b[x + y] = c[x - y + N - 1] = True
                dfs(x + 1)
                a[y] = b[x + y] = c[x - y + N - 1] = False

for tc in range(1, int(input()) + 1):
    N = int(input())
    a = [False] * N
    b = [False] * (2 * N - 1)   # 대각선 /: X + Y
    c = [False] * (2 * N - 1)   # 대각선 \: X - Y + N - 1
    result = 0
    dfs(0)
    print(f'#{tc} {result}')