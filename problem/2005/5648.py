# SWEA 5648 원자 소멸 시뮬레이션
# 메모리 초과

for tc in range(1, int(input()) + 1):
    N = int(input())
    atom = []
    visited = [[0] * 4002 for _ in range(4002)]
    for n in range(N):
        temp = list(map(int, input().split()))
        temp[0] = (temp[0] + 1000) * 2
        temp[1] = (temp[1] + 1000) * 2
        atom.append([temp[0], temp[1], temp[2], temp[3]])
        visited[temp[1]][temp[0]] += 1

    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]
    energy = 0
    while atom:
        crash = []
        for a in range(len(atom)):
            visited[atom[a][1]][atom[a][0]] -= 1
            atom[a][0] = atom[a][0] + dx[atom[a][2]]
            atom[a][1] = atom[a][1] + dy[atom[a][2]]
            if 0 <= atom[a][0] <= 4000 and 0 <= atom[a][1] <= 4000:
                visited[atom[a][1]][atom[a][0]] += 1
            else:
                crash.append(a)
        for a in range(len(atom)):
            if a not in crash:
                x, y, d, e = atom[a]
                if visited[y][x] > 1:
                    crash.append(a)
                    energy += e
        crash.sort(reverse=True)
        for c in crash:
            x, y, d, e = atom.pop(c)
            if 0 <= y <= 4000 and 0 <= x <= 4000:
                visited[y][x] -= 1
    print(f'#{tc} {energy}')