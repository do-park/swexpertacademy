# SWEA 5521 상원이의 생일파티

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    friends = [[] for _ in range(N + 1)]
    invited = [0] * (N + 1)
    invited[1] = 1
    for m in range(M):
        a, b = map(int, input().split())
        friends[a].append(b)
        friends[b].append(a)
    for i in friends[1]:
        invited[i] = 1
        for j in friends[i]:
            invited[j] = 1
    print(f'#{tc} {sum(invited) - 1}')