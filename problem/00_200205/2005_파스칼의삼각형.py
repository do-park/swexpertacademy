T = int(input())

for tc in range(T):

    N = int(input())

    pascal = [[1 for _ in range(i)] for i in range(1, N + 1)]

    for i in range(2, N):
        for j in range(1, i):
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

    print('#{}'.format(tc + 1))
    for i in range(N):
        for j in range(0, i + 1):
            print(pascal[i][j], end=' ')
        print()