from collections import deque

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    oven = deque()
    result = -1
    for n in range(N):
        oven.append(n)
    while oven:
        x = oven.popleft()
        pizza[x] //= 2
        if pizza[x]:
            oven.append(x)
        else:
            if n + 1 < M:
                oven.append(n + 1)
                n += 1
    print(f'#{tc} {x + 1}')