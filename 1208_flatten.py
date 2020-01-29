def myMax (data):
    mymax = 0
    mymax_idx = 0
    for i in range(0, len(data)):
        if mymax < data[i]:
            mymax = data[i]
            mymax_idx = i
    return mymax, mymax_idx


def myMin (data):
    mymin = 100
    mymin_idx = 0
    for i in range(0, len(data)):
        if mymin > data[i]:
            mymin = data[i]
            mymin_idx = i
    return mymin, mymin_idx



import sys
sys.stdin = open("test.txt", "r")

T = 10
for tc in range(T):
    N = int(input())        # 덤프 횟수
    data = list(map(int, input().split()))
    max_data, max_data_idx = myMax(data)
    min_data, min_data_idx = myMin(data)
    ans = max_data - min_data

    for i in range(0, N):
        data[max_data_idx] -= 1
        data[min_data_idx] += 1
        max_data, max_data_idx = myMax(data)
        min_data, min_data_idx = myMin(data)
        ans = max_data - min_data

        if (ans == 0) or (ans == 1):
            break

    print("#{} {}".format(tc + 1, ans))     #정답
