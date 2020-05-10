# SWEA 1206 View

for tc in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    result = 0
    for n in range(2, N - 2):
        highest = buildings[n]
        around = max(buildings[n - 2], buildings[n - 1], buildings[n + 1], buildings[n + 2])
        result = result + (highest - around) if highest > around else result
    print(f'#{tc} {result}')