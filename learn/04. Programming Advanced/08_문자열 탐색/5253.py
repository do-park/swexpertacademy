# SWEA 5253 접두어 검색

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    A = [input() for _ in range(N)]
    B = [input() for _ in range(M)]
    result = 0
    for b in B:
        for a in A:
            if a.find(b) == 0:
                result += 1
                break
    print(f'#{tc} {result}')