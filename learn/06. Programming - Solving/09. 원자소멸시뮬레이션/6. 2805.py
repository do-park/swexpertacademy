# SWEA 2805 농작물 수확하기

for tc in range(1, int(input()) + 1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    result = 0
    j = N // 2
    for i in range(N):
        if i == 0:
            a = N // 2
            b = a + 1
            result += sum(farm[i][a:b])
        elif i <= j:
            a -= 1
            b += 1
            result += sum(farm[i][a:b])
        else:
            a += 1
            b -= 1
            result += sum(farm[i][a:b])
    print(f'#{tc} {result}')