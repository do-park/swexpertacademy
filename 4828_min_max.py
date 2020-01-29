T = int(input())

for i in range(0, T):
    N = int(input())
    list_a = list(map(int, input().split()))
    min_a = list_a[0]
    max_a = list_a[0]
    for j in range(1, N):
        if min_a > list_a[j]:
            min_a = list_a[j]
        if max_a < list_a[j]:
            max_a = list_a[j]
    print('#{} {}'.format(i+1, (max_a - min_a)))