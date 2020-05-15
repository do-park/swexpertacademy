# SWEA 5209 최소 생산 비용
# Fail (Runtime error), 5/10 pass

from itertools import permutations

for tc in range(1, int(input()) + 1):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]
    P = list(permutations([n for n in range(N)]))
    answer = 1500
    for p in P:
        result = 0
        for n in range(N):
            result += maps[n][p[n]]
            if result > answer:
                break
        else:
            answer = min(answer, result)
    print(f'#{tc} {answer}')