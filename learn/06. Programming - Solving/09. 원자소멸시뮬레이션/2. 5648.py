# SWEA 5648 원자 소멸 시뮬레이션

for tc in range(1, int(input()) + 1):
    N = int(input())
    atom = []
    for n in range(N):
        temp = list(map(int, input().split()))
        temp[0] = (temp[0] + 1000) * 2
        temp[1] = (temp[1] + 1000) * 2
        atom.append([temp[0], temp[1], temp[2], temp[3]])
    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]
    energy = 0
    while len(atom) >= 2:
        visited = {}
        crash = []
        for a in range(len(atom)):
            atom[a][0] = atom[a][0] + dx[atom[a][2]]
            atom[a][1] = atom[a][1] + dy[atom[a][2]]
            if 0 <= atom[a][0] <= 4000 and 0 <= atom[a][1] <= 4000:
                loc = '{} {}'.format(atom[a][0], atom[a][1])
                if visited.get(loc):
                    visited[loc].append(atom[a])
                else:
                    visited[loc] = [atom[a]]
            else:
                crash.append(atom[a])
        for v in visited:
            if len(visited[v]) > 1:
                for i in visited[v]:
                    crash.append(i)
                    energy += i[3]
        for c in crash:
            atom.remove(c)
    print(f'#{tc} {energy}')