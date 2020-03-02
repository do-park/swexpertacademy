from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    answer = -1
    result = -1
    for i in range(N):
        for j in range(N):
            Q = deque()
            Q.append([i, j])
            cnt = 1
            while Q:
                [y, x] = Q.popleft()
                for d in range(4):
                    Y = y + dy[d]
                    X = x + dx[d]
                    if 0 <= X < N and 0 <= Y < N and maps[y][x] + 1 == maps[Y][X]:
                        Q.append([Y, X])
                        cnt += 1
            if result < cnt:
                answer = maps[i][j]
                result = cnt
            elif result == cnt:
                if answer > maps[i][j]:
                    answer = maps[i][j]

    print(f'#{tc} {answer} {result}')
