dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def f(y, x, k, res):
    if k == 7:
        s.add(res)
    else:
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < 4 and 0 <= nx < 4:
                f(ny, nx, k + 1, res * 10 + arr[ny][nx])

T = int(input())
for tc in range(1, T + 1):
    s = set()
    arr = [list(map(int, input().split())) for _ in range(4)]
    for i in range(4):
        for j in range(4):
            f(i, j, 1, arr[i][j])
    print(s)
    print(f'#{tc} {len(s)}')