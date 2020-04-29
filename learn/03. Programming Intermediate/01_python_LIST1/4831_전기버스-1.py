for tc in range(1, int(input()) + 1):
    K, N, M = map(int, input().split())
    pos = list(map(int, input().split()))

    station = [0] * (N + 1)
    for p in pos:
        station[p] = 1

    bus = ans = 0
    while bus + K < N :
        for p in range(bus + K, bus, -1):
            if station[p]:
                bus = p
                ans += 1
                break
        else:
            ans = 0
            break
    print(f'#{tc} {ans}')