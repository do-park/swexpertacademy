di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def f(N, M, K, org):
    d = K // 2
    ts = [[-1] * (M + K) for _ in range(N + K)]  # timestamp
    cell = [[0] * (M + K) for _ in range(N + K)]  # 줄기세포
    for i in range(N):
        for j in range(M):
            cell[i + d][j + d] = org[i][j]
            if org[i][j] != 0:
                ts[i + d][j + d] = 0
    for h in range(1, K + 1):
        for i in range(d - h // 2, N + d + h // 2):
            for j in range(d - h // 2, M + d + h // 2):
                tmp = []  # 주변의 활성세포 생명력 리스트
                if cell[i][j] == 0:  # 아직 세포가 없으면
                    for k in range(4):
                        ni = i + di[k]
                        nj = j + dj[k]
                        if 0 <= ni < N + K and 0 <= nj < M + K:
                            if cell[ni][nj] > 0 and ((h - ts[ni][nj]) / cell[ni][nj]) > 1:  # 활성세포가 있으면
                                tmp.append(cell[ni][nj])  # 생명력 리스트 만듦
                if tmp:
                    cell[i][j] = max(tmp)  # 세포 생성
                    ts[i][j] = h  # 세포 생성 시간 기록
    cnt = 0
    for i in range(N + K):
        for j in range(M + K):
            if cell[i][j] > 0 and (K - ts[i][j]) // cell[i][j] < 2:
                cnt += 1
    return cnt


T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    org = [list(map(int, input().split())) for _ in range(N)]
    r = f(N, M, K, org)
    print(f'#{tc} {r}')


