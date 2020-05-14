# SWEA 5204 병합 정렬

from collections import deque

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    global count
    result = []
    lQ = deque()
    rQ = deque()
    lQ.extend(left)
    rQ.extend(right)
    if lQ[-1] > rQ[-1]:
        count += 1
    while lQ or rQ:
        if lQ and rQ:
            if lQ[0] <= rQ[0]:
                result.append(lQ.popleft())
            else:
                result.append(rQ.popleft())
        elif lQ:
            result.extend(lQ)
            break
        elif rQ:
            result.extend(rQ)
            break
    return result

for tc in range(1, int(input()) + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    count = 0
    result = merge_sort(numbers)
    print(f'#{tc} {result[N // 2]} {count}')