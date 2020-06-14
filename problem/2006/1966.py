# 1966 숫자를 정렬하자

for tc in range(1, int(input()) + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    numbers = sorted(numbers)
    print(f'#{tc}', end=' ')
    for n in range(N):
        print(numbers[n], end=' ')
    print()