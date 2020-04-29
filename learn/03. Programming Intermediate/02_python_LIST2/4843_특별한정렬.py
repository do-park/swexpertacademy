import sys
sys.stdin = open("4843_특별한정렬.txt", "r")

T = int(input())

for tc in range(T):
    N = int(input())
    ans = 0
    data = list(map(int, input().split()))
    data.sort()

    new_data = []
    while data:
        new_data.append(data[-1])
        del data[-1]
        new_data.append(data[0])
        del data[0]

    print("#{}".format(tc + 1), end='')     #정답
    for i in range(0, 10):
        print(" {}".format(new_data[i]), end='')
    print()