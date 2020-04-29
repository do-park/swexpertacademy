# SWEA 5186 이진수2

for tc in range(1, int(input()) + 1):
    N = float(input())
    result = ''
    for i in range(1, 13):
        if N >= (1 / (2 ** i)):
            result += '1'
            N -= (1 / (2 ** i))
            if not N:
                break
        else:
            result += '0'
    else:
        result = 'overflow'
    print(f'#{tc} {result}')