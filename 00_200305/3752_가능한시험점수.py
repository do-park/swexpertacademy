T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    scores = list(map(int, input().split()))
    maxS = sum(scores) + 1
    results = [0] * (maxS)
    results[0] = 1
    for n in range(N):
        temp = [0] * (maxS)
        for i in range(maxS):
            if results[i]:
                temp[i + scores[n]] = 1
        for i in range(maxS):
            results[i] = max(results[i], temp[i])
    print(f'#{tc} {sum(results)}')