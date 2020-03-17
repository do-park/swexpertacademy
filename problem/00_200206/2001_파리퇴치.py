import sys
sys.stdin = open("파리퇴치.txt", "r")


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]

    results = []
    for i in range(0, N - M + 1):
        for j in range(0, N - M + 1):
            sum = 0
            for x in range(0, M):
                for y in range(0, M):
                    sum += flies[i+x][j+y]
            results.append(sum)

    print('#{} {}'.format(tc, max(results)))