# SWEA 5208 전기버스(2)

def solution(now=1, battery=0, change=-1):
    global result
    if change > result:
        return
    if now == stops[0]:
        result = min(result, change)
        return
    if battery:
        solution(now + 1, battery - 1, change)
    solution(now + 1, stops[now] - 1, change + 1)


for tc in range(1, int(input()) + 1):
    stops = list(map(int, input().split()))
    result = stops[0]
    solution()
    print(f'#{tc} {result}')