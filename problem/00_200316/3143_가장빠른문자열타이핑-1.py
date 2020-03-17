for tc in range(1, int(input()) + 1):
    A, B = input().split()
    t = A.count(B)
    print(f'#{tc} {len(A) - t * len(B) + t}')