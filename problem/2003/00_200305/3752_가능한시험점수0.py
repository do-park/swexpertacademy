T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    scores = list(map(int, input().split()))
    maxS = sum(scores) + 1
    results = [0] * (maxS)
    results[0] = 1
    for n in range(N):
        for i in range(maxS - 1, -1, -1):
            if results[i]:
                results[i + scores[n]] = 1
    print(f'#{tc} {sum(results)}')