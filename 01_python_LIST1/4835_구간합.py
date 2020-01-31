T = int(input())

for i in range(0, T):
    N, M = input().split()
    N = int(N); M = int(M)
    numbers = list(map(int, input().split()))

    results = []
    for j in range(0, N - M + 1):

        result = 0
        for k in range(0, M):
            result += numbers[j+k]
        results.append(result)

    max_result = results[0]
    min_result = results[0]

    for x in results:
        if x > max_result:
            max_result = x
        if x < min_result:
            min_result = x


    print('#{} {}'.format(i+1, max_result - min_result))