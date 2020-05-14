# SWEA 5205 퀵 정렬

for tc in range(1, int(input()) + 1):
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted(A)
    print(f'#{tc} {A[N//2]}')