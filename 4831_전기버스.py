def Reverse(a):
    new = []
    for i in range(len(a)-1, -1, -1):
        new.append(a[i])
    return new


T = int(input())
for tc in range(0, T):
    K, N, M = map(int, input().split())
    M_list = list(map(int, input().split()))
    M_list = Reverse(M_list)
    M_list += [0, 0]

    bus = N
    count = 0

    for i in range(0, M):
        if bus - M_list[i] > K:
            count = 0
            break
        else:
            if bus - M_list[i+1] > K:
                count += 1
                bus = M_list[i]
        if bus <= K:
            break

    print('#{} {}'.format(tc + 1, count))