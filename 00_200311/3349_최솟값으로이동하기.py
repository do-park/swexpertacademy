T = int(input())

for tc in range(1, T + 1):
    W, H, N = list(map(int, input().split()))
    result = 0
    x1, y1 = map(int, input().split())
    for n in range(N - 1):
        x2, y2 = map(int, input().split())
        if (x1 < x2 and y1 < y2) or (x1 > x2 and y1 > y2):
            if abs(x1 - x2) == abs(y1 - y2):
                result += abs(x1 - x2)
            elif abs(x1 - x2) > abs(y1 - y2):
                result += abs(y1 - y2) + abs(abs(x1 - x2) - abs(y1 - y2))
            else:
                result += abs(x1 - x2) + abs(abs(x1 - x2) - abs(y1 - y2))
        else:
            result += abs(x1 - x2) + abs(y1 - y2)
        x1, y1 = x2, y2
    print(f'#{tc} {result}')