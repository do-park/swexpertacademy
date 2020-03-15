for tc in range(1, int(input()) + 1):
    K, N, M = map(int, input().split())
    pos = [0] + list(map(int, input().split())) + [N]

    bus = ans = 0

    for i in range(1, M + 2):
        if pos[i] - pos[i - 1] > K:
            ans = 0;
            break
        if bus + K < pos[i]:
            bus = pos[i - 1]
            ans += 1
    print(f'#{tc} {ans}')