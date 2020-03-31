from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    num = deque(list(map(str, input())))
    L = N // 4
    temp = ''
    result = []
    for l in range(L):
        for i in range(0, N, L):
            for j in range(L):
                temp += num[i + j]
            if temp not in result:
                result.append(temp)
            temp = ''
        num.append(num[0])
        num.popleft()
    result.sort(reverse=True)

    temp = list(result[K - 1])
    ans = 0
    for t in temp:
        if 'A' <= t <= 'F':
            t = (ord(t) - ord('A')) + 10
        ans = ans * 16 + int(t)

    print(f'#{tc} {ans}')