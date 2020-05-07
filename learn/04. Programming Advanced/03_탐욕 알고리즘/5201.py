# SWEA 5201 컨테이너 운반

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    containers = sorted(containers)
    trucks = sorted(trucks)
    result = 0
    while True:
        if not containers or not trucks:
            break
        if trucks[-1] >= containers[-1]:
            result += containers[-1]
            trucks.pop()
            containers.pop()
        else:
            containers.pop()
    print(f'#{tc} {result}')