import sys
sys.stdin = open("4615_재미있는오셀로게임.txt", "r")


def safe(x,y):
    return N > x >= 0 and N > y >= 0


def CC(A,B,C,dx,dy):
        tmp = []
        for i in range(N):
            A += dx
            B += dy
            if safe(A, B):
                tmp.append((A, B))
                if area[A][B] == 0:
                    break
                elif area[A][B] == C:
                    while tmp:
                        n = tmp.pop()
                        area[n[0]][n[1]] = C
                    break



T = int(input())

for tc in range(1,1+T):
    N, M = map(int, input().split())
    area = [[0 for x in range(N)] for y in range(N)]
    # 1이 블랙 2가 화이트
    for i in range(2):
        area[N // 2 - i][N // 2 - 1 + i] = 1
        area[N // 2 - i][N // 2 - i] = 2

    dy = [1,-1,0,0,1,-1,-1,1]
    dx = [0,0,1,-1,1,-1,1,-1]

    for i in range(M):
        X, Y, Z = map(int, input().split())
        X -= 1
        Y -= 1
        area[X][Y] = Z
        for j in range(8):
            CC(X, Y, Z, dy[j], dx[j])
    black = 0
    white = 0
    for i in area:
        black += i.count(1)
        white += i.count(2)

    print('#{} {} {}'.format(tc, black, white))