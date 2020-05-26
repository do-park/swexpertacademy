# SWEA 1974 스도쿠 검증

for tc in range(1, int(input()) + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    result = True
    # 가로
    for i in range(9):
        if result:
            numbers = [0] * 10
            for j in range(9):
                numbers[sudoku[i][j]] += 1
                if numbers[sudoku[i][j]] > 1:
                    result = False
                    break
    # 세로
    if result:
        for i in range(9):
            if result:
                numbers = [0] * 10
                for j in range(9):
                    numbers[sudoku[j][i]] += 1
                    if numbers[sudoku[j][i]] > 1:
                        result = False
                        break
    # 3 * 3
    if result:
        for y in range(0, 9, 3):
            for x in range(0, 9, 3):
                if result:
                    numbers = [0] * 10
                    for i in range(3):
                        for j in range(3):
                            ty = y + i
                            tx = x + j
                            numbers[sudoku[y + i][x + j]] += 1
                            if numbers[sudoku[y + i][x + j]] > 1:
                                result = False
                                break

    print(f'#{tc} {int(result)}')