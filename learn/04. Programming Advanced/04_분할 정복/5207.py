# SWEA 5207 이진 탐색

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    count = 0
    for b in B:
        l = 0
        r = N - 1
        flag = 0
        while l <= r:
            m = (l + r) // 2
            if A[m] == b:
                count += 1
                break
            elif A[m] > b:
                r = m - 1
                if flag == -1:
                    break
                flag = -1
            elif A[m] < b:
                l = m + 1
                if flag == 1:
                    break
                flag = 1
    print(f'#{tc} {count}')