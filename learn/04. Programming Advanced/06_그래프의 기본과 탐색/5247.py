# SWEA 5247 연산

from collections import deque

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    q = deque()
    visited = [0] * 1000001
    q.append(N)
    visited[N] = 1
    while q:
        x = q.popleft()
        if x == M:
            print(f'#{tc} {visited[M] - 1}')
            break
        for i in [x + 1, x - 1, x * 2, x - 10]:
            if 0 < i < 1000001 and not visited[i]:
                visited[i] = visited[x] + 1
                q.append(i)
