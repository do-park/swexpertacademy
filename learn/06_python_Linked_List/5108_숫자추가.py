for tc in range(1, int(input()) + 1):
    N, M, L = map(int, input().split())
    numbers = list(map(int, input().split()))
    for m in range(M):
        idx, num = map(int, input().split())
        numbers.insert(idx, num)
    print(f'#{tc} {numbers[L]}')