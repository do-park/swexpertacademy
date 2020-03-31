for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = [0] * N
    for m in range(M):
        for n in range(N):
            if B[m] >= A[n]:
                result[n] += 1
                break
    print(f'#{tc} {result.index(max(result)) + 1}')