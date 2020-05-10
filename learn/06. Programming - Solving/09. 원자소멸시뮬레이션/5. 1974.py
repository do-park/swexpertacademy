# SWEA 1974 스도쿠 검증

def garo():
    for i in range(9):
        visited = [0] * 10
        for j in range(9):
            if visited[sudoku[i][j]] == 1:
                return 0
            else:
                visited[sudoku[i][j]] += 1
    return 1

def sero():
    for j in range(9):
        visited = [0] * 10
        for i in range(9):
            if visited[sudoku[i][j]] == 1:
                return 0
            else:
                visited[sudoku[i][j]] += 1
    return 1

def mini():
    for i in range(3):
        for j in range(3):
            visited = [0] * 10
            for y in range(3):
                for x in range(3):
                    if visited[sudoku[i * 3 + y][j * 3 + x]]:
                        return 0
                    else:
                        visited[sudoku[i * 3 + y][j * 3 + x]] += 1
    return 1


for tc in range(1, int(input()) + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    result = garo()
    if result:
        result = sero()
    if result:
        result = mini()
    print(f'#{tc} {result}')