from collections import deque

for tc in range(1, int(input()) + 1):
    H, W = map(int, input().split())
    castle = []
    visited = [[0] * W for _ in range(H)]
    Q = deque()
    for h in range(H):
        temp = list(map(str, input()))
        for w in range(W):
            if temp[w] == '.':
                temp[w] = 0
                Q.append((h, w))
                visited[h][w] = 1
            else:
                temp[w] = int(temp[w])
        castle.append(temp)
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    cnt = 0
    while True:
        tQ = deque()
        diff = 0
        while Q:
            y, x = Q.popleft()
            loss = 0
            for d in range(8):
                ny = y + dy[d]
                nx = x + dx[d]
                if 0 <= ny < H and 0 <= nx < W and not visited[ny][nx] and castle[ny][nx]:
                    castle[ny][nx] -= 1
                    if not castle[ny][nx]:
                        tQ.append((ny, nx))
                        visited[ny][nx] = 1
        Q = tQ
        if not Q:
            break
        cnt += 1
    print(f'#{tc} {cnt}')