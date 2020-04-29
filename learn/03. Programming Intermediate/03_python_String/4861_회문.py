def is_palindrome(N, board):
    count = 0
    for n in range(0, 100):
        for i in range(0, 101 - N):
            for j in range(0, N // 2):
                if board[n][i + j] != board[n][i + N - j - 1]:
                    break
            else:
                count += 1

    return count


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = []
    result = []
    for n in range(0, N):
        board.append(input())
        for i in range(0, N - M + 1):
            for j in range(0, N // 2):
                if board[n][i + j] != board[n][i + M - j - 1]:
                    break
            else:
                result.append(board[n][i:M + i])

    new_brd = [[] for _ in range(0, N)]

    for x in range(0, N):
        for y in range(0, N):
            new_brd[x].append(board[y][x])

    for n in range(0, N):
        for i in range(0, N - M + 1):
            for j in range(0, N // 2):
                if new_brd[n][i + j] != new_brd[n][i + M - j - 1]:
                    break
            else:
                temp = new_brd[n][i:M + i]
                t2s = ''
                for t in temp:
                    t2s += t
                result.append(t2s)

    print('#{} {}'.format(tc, result[0]))