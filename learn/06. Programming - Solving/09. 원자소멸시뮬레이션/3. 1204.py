# SWEA 1204 최빈수 채우기

import operator

for tc in range(int(input())):
    N = int(input())
    students = list(map(int, input().split()))
    scores = {}
    for i in range(1000):
        if students[i] in scores:
            scores[students[i]] += 1
        else:
            scores[students[i]] = 1
    sdict = sorted(scores.items(), key=operator.itemgetter(1), reverse=True)
    result = sdict[0][0]
    print(f'#{N} {result}')