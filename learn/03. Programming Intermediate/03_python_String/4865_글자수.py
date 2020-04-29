T = int(input())

for tc in range(1, T + 1):
    str1 = list(input())
    str2 = list(input())

    dic = {}
    for s in str1:
        if s not in dic:
            dic[s] = 0

    for s in str2:
        if s in dic:
            dic[s] += 1

    print('#{} {}'.format(tc, max(dic.values())))