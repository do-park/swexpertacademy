def Left(x, y):
    global now, cnt
    for l in range(1, 100):
        if y - l < 0:
            now = 0
            break
        else:
            if area[x][y - l] == 0:
                now = y - l + 1
                break
        cnt += 1
    return now


def Right(x, y):
    global now, cnt
    for l in range(1, 100):
        if y + l > 99:
            now = 99
            break
        else:
            if area[x][y + l] == 0:
                now = y + l - 1
                break
        cnt += 1
    return now


def ladder(num):
    global cnt
    now = num
    for i in range(1, 100):
        left = now - 1
        right = now + 1
        if left > 0 and area[i][left] == 1:
            now = Left(i, now)
        elif right < 99 and area[i][right] == 1:
            now = Right(i, now)
        cnt += 1


for _ in range(1, 11):
    case = int(input())
    start = []
    area = []
    shorti = 987654321
    result = 0
    for i in range(100):
        area.append(list(map(int, input().split())))
        if area[0][i] == 1:
            start.append(i)

    for start_num in start:
        cnt = 0
        ladder(start_num)
        if cnt <= shorti:
            shorti = cnt
            result = start_num
    print('#{} {}'.format(case, result))
