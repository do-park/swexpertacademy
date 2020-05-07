# SWEA 5189 전자카트

from itertools import permutations
from math import inf

for tc in range(1, int(input()) + 1):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]
    num = [_ for _ in range(1, N)]
    perm = list(permutations(num, N - 1))
    result = inf
    for p in perm:
        temp = maps[0][p[0]] + maps[p[-1]][0]
        for i in range(N - 2):
            temp += maps[p[i]][p[i + 1]]
        if temp < result:
            result = temp
    print(f'#{tc} {result}')