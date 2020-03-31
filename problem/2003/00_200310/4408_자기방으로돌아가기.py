for tc in range(1, int(input()) + 1):
    room = [0] * 201
    N = int(input())
    for n in range(N):
        s, e = map(int, input().split())
        if s > e:
            s, e = e, s
        if s % 2:
            s += 1
        if e % 2:
            e += 1
        s, e = s//2, e//2

        for i in range(s, e + 1):
            room[i] += 1
    print(f'#{tc} {max(room)}')