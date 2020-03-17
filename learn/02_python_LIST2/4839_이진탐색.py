import sys
sys.stdin = open("4839_이진탐색.txt", "r")


def binarySearch(pages, key):
    left = 1; right = pages
    count = 0
    while left <= right:
        mid = (left + right) // 2
        if key == mid:
            return count
        elif key < mid:
            right = mid
            count += 1
        else:
            left = mid
            count += 1
    return count


T = int(input())

for tc in range(T):
    mylist = list(map(int, input().split()))        # P: 책의 전체 쪽수, A: A가 찾을 쪽 번호, B: B가 찾을 쪽 번호

    resA = binarySearch(mylist[0], mylist[1])
    resB = binarySearch(mylist[0], mylist[2])

    if resA < resB:
        result = 'A'
    elif resA > resB:
        result = 'B'
    else:
        result = 0

    print('#{} {}'.format(tc + 1, result))