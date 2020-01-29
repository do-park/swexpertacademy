T = int(input())

for i in range(0, T):
    N = int(input())
    A = int(input())
    list_a = [0] * 10
    mode = 0
    mode_freq = 0
    for j in range(0, N):
        list_a[A % 10] += 1
        if list_a[A % 10] > mode_freq:
            mode = A % 10
            mode_freq = list_a[mode]
        elif list_a[A % 10] == mode_freq:
            if mode < (A % 10):
                mode = A % 10
        A //= 10
    print('#{} {} {}'.format(i+1, mode, mode_freq))