for tc in range(1, int(input()) + 1):
    A, B = input().split()
    a, b = len(A), len(B)
    cnt = i = 0
    while i < a:
        if A[i] == B[0] and i + b <= a:
            for j in range(0, b):
                if A[i + j] != B[j]:
                    break
                if j == b - 1:
                    i += b - 1
        cnt += 1
        i += 1
    print(f'#{tc} {cnt}')