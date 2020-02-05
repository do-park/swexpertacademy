T = int(input())

for tc in range(1, T + 1):
    num = int(input())
    num_list = list(map(int, input().split()))
    danjo_list = []
    for i in range(len(num_list) - 1):
        for j in range(i + 1, len(num_list)):
            danjo_list.append(num_list[i] * num_list[j])
    danjo_list.sort()
    for i in range(len(danjo_list) - 1, -1, -1):
        target = str(danjo_list[i])
        for i in range(len(target) - 1):
            if target[i] > target[i + 1]:
                break
        else:
            result = int(target)
            break
    else:
        result = -1
    print('#{} {}'.format(tc, result))