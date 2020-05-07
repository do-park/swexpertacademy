# SWEA 5202 화물 도크

for tc in range(1, int(input()) + 1):
    N = int(input())
    docks = [list(map(int, input().split())) for _ in range(N)]
    docks = sorted(docks, key=lambda x:(x[1], x[0]))
    count = 0
    end = 0
    for dock in docks:
        if dock[0] >= end:
            count += 1
            end = dock[1]
    print(f'#{tc} {count}')