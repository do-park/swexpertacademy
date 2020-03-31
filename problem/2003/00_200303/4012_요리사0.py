bitCnt = [[] for _ in range(9)]
for i in range(1, 1 << 16):
    cnt = 0
    for j in range(16):
        if i & (1 << j) != 0:
            cnt += 1
    if cnt <= 8:
        bitCnt[cnt].append(i)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    synergy = [0] * (1 << N)
    for x in bitCnt[2]:
        if x < (1 << N):
            one = []
            for i in range(N):
                if x & (1 << i) != 0:
                    one.append(i)
            synergy[x] = arr[one[0]][one[1]] + arr[one[1]][one[0]]

        for y in range(3, N // 2 + 1):
            for x in bitCnt[y]:
                if x < (1 << N):
                    for i in range(N):
                        if (x & (1 << i)) != 0:
                            first = i
                            break
                    synergy[x] += synergy[~(1 << first) & x]
                    for i in range(first + 1, N):
                        if (x & (1 << i)) != 0:
                            synergy[x] += synergy[(1 << first) | (1 << i)]

    diff = []
    for x in bitCnt[N // 2]:
        if x < (1 << N):
            diff.append(abs(synergy[x] - synergy[(1 << N) - 1 - x]))
    print('#{} {}'.format(tc, min(diff)))