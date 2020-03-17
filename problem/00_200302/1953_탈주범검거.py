from collections import deque

def up(y, x):
    Y, X = y - 1, x
    if 0 <= Y < N and 0 <= X < M and not visited[Y][X] and (maps[Y][X] == 1 or maps[Y][X] == 2 or maps[Y][X] == 5 or maps[Y][X] == 6):
        Q_temp.append([Y, X])
        visited[Y][X] = True

def down(y, x):
    Y, X = y + 1, x
    if 0 <= Y < N and 0 <= X < M and not visited[Y][X] and (maps[Y][X] == 1 or maps[Y][X] == 2 or maps[Y][X] == 4 or maps[Y][X] == 7):
        Q_temp.append([Y, X])
        visited[Y][X] = True

def left(y, x):
    Y, X = y, x - 1
    if 0 <= Y < N and 0 <= X < M and not visited[Y][X] and (maps[Y][X] == 1 or maps[Y][X] == 3 or maps[Y][X] == 4 or maps[Y][X] == 5):
        Q_temp.append([Y, X])
        visited[Y][X] = True

def right(y, x):
    Y, X = y, x + 1
    if 0 <= Y < N and 0 <= X < M and not visited[Y][X] and (maps[Y][X] == 1 or maps[Y][X] == 3 or maps[Y][X] == 6 or maps[Y][X] == 7):
        Q_temp.append([Y, X])
        visited[Y][X] = True


T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    Q, Q_temp = deque(), deque()
    Q.append([R, C])
    visited[R][C] = True
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    for l in range(1, L):
        while Q:
            y, x = Q.popleft()
            if maps[y][x] == 1:
                up(y, x)
                down(y, x)
                left(y, x)
                right(y, x)
            elif maps[y][x] == 2:
                up(y, x)
                down(y, x)
            elif maps[y][x] == 3:
                left(y, x)
                right(y, x)
            elif maps[y][x] == 4:
                up(y, x)
                right(y, x)
            elif maps[y][x] == 5:
                right(y, x)
                down(y, x)
            elif maps[y][x] == 6:
                left(y, x)
                down(y, x)
            elif maps[y][x] == 7:
                up(y, x)
                left(y, x)
        Q = Q_temp
        Q_temp = deque()
    cnt = 0
    for n in range(N):
        for m in range(M):
            if visited[n][m]:
                cnt += 1
    print(f'#{tc} {cnt}')