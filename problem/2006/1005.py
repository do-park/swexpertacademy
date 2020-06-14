# 1970 쉬운 거스름돈

money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for tc in range(1, int(input()) + 1):
    N = int(input())
    result = []
    for m in money:
        result.append(N // m)
        N %= m
    print(f'#{tc}')
    print(* result)