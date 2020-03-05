def remove(c, N, W, H, br):
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    q = []
    r = 0
    while r < H and br[r][c] == 0:  # 맨 위 벽돌 찾기
        r += 1
    if r == H:  # 벽돌이 없는 경우
        return
    q.append((r, c))

    while (len(q) != 0):
        i, j = q.pop(0)
        k = br[i][j]  # 벽돌의 제거 범위
        br[i][j] = 0
        for dis in range(1, k):
            for dir in range(4):  # 4방향
                ni = i + dis * di[dir]
                nj = j + dis * dj[dir]
                if 0 <= ni < H and 0 <= nj < W:
                    q.append((ni, nj))


def shoot(N, W, H):
    br = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            br[i][j] = org[i][j]
    for i in range(N):
        remove(p[i], N, W, H, br)

        for i in range(W):  # 아래로 떨어뜨릴 벽돌 찾기
            st = []
            for j in range(H - 1, -1, -1):
                if br[j][i] != 0:
                    st.append(br[j][i])
                    br[j][i] = 0
            for j in range(0, len(st)):
                br[H - 1 - j][i] = st[j]
    cnt = 0
    for i in range(H):
        for j in range(W):
            if br[i][j] != 0:  # 벽돌이 남아있으면
                cnt += 1
    return cnt


def npr(n, k, W, H):
    global minV
    if n == k:
        r = shoot(k, W, H)  # 구슬을 발사, 남은 벽돌 수 리턴
        if minV > r:
            minV = r
    else:
        for i in range(W):  # 중복순열
            p[n] = i
            npr(n + 1, k, W, H)
            if minV == 0:
                return


T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    org = [list(map(int, input().split())) for _ in range(H)]  # 초기 벽돌 상태
    p = [0] * N  # 구슬을 쏠 가로 위치 (N번)
    minV = 10 ** 9
    npr(0, N, W, H)
    print('#{} {}'.format(tc, minV))
