from collections import deque

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    Q = deque(list(map(int, input().split())))
    for m in range(M):
        x = Q.popleft()
        Q.append(x)
    print(f'#{tc} {Q.popleft()}')