import sys
sys.stdin = open("5356_의석이의세로로말해요.txt", "r")


T = int(input())

for tc in range(1, T + 1):
    board = [list(map(str, input())) for _ in range(5)]

    result = []
    for i in range(0, 15):
        for j in range(0, 5):
            if i < len(board[j]):
                result.append(board[j][i])

    print('#{} '.format(tc), end='')
    for i in range(len(result)):
        print('{}'.format(result[i]), end='')
    print()