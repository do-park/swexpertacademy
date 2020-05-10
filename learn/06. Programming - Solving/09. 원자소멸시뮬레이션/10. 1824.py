# SWEA 1824 혁진이의 프로그램 검증
# 마지막 예제가 실행되지 않는다.
# 그리고 SWEA는 sys import 불가능할걸?

import sys
sys.setrecursionlimit(1000000)


def bly(y=0, x=0, d=3, m=0, depth=0):
    ret = False
    if cmd[y][x].isdecimal():
        m = int(cmd[y][x])
    elif cmd[y][x] == '>' or (cmd[y][x] == '_' and m == 0):
        d = 3
    elif cmd[y][x] == '<' or (cmd[y][x] == '_'):
        d = 2
    elif cmd[y][x] == 'v' or (cmd[y][x] == '|' and m == 0):
        d = 1
    elif cmd[y][x] == '^' or cmd[y][x] == '|':
        d = 0
    elif cmd[y][x] == '+':
        m = (m + 1) % 16
    elif cmd[y][x] == '-':
        m = (m + 16 - 1) % 16
    elif cmd[y][x] == '@':
        return True

    if check[y][x][d][m]:
        return False
    else:
        check[y][x][d][m] = 1

    ny = (y + dy[d] + R) % R
    nx = (x + dx[d] + C) % C

    if cmd[y][x] == '?':
        for dir in range(4):
            ny = (y + dy[dir] + R) % R
            nx = (x + dx[dir] + C) % C
            ret = bly(ny, nx, dir, m, depth + 1) or ret
        return ret
    else:
        return bly(ny, nx, d, m, depth + 1) or ret


for tc in range(1, int(input()) + 1):
    R, C = map(int, input().split())
    cmd = [list(map(str, input())) for _ in range(R)]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    check = [[[[0] * 16 for _ in range(4)] for c in range(C)] for r in range(R)]
    print(f'#{tc} ', end='')
    print('YES' if bly() else 'NO')