T = int(input())

for tc in range(1, T + 1):
    str1 = list(map(str, input()))
    str2 = list(map(str, input()))
    len1 = len(str1); len2 = len(str2)

    flag = 0
    for i in range(0, len2 - len1 + 1):
        for j in range(0, len1):
            if str1[j] != str2[i + j]:
                break
        else:
            flag = 1
            break

    if flag:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))
