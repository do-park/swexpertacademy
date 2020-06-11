# SWEA 1859 백만 장자 프로젝트

for tc in range(1, int(input()) + 1):
    N = int(input())
    price = list(map(int, input().split()))
    M = 0
    result = 0
    for n in range(N - 1, -1, -1):
        if price[n] > M:
            M = price[n]
        result += M - price[n]
    print(f'#{tc} {result}')