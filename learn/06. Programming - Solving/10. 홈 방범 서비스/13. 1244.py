# SWEA 1244 최대 상금

def getNum():
    number = 0
    for n in numbers:
        number = number * 10 + n
    return number

def backtracking(k):
    number = getNum()
    if number in visited[k & 1]:
        return
    visited[k & 1].add(number)
    if k == K:
        return
    else:
        for i in range(L - 1):
            for j in range(i + 1, L):
                numbers[i], numbers[j] = numbers[j], numbers[i]
                backtracking(k + 1)
                numbers[i], numbers[j] = numbers[j], numbers[i]


for tc in range(1, int(input()) + 1):
    numbers, K = map(str, input().split())
    numbers = list(map(int, numbers))
    L = len(numbers)
    K = int(K)
    visited = [set() for _ in range(2)]
    backtracking(0)
    print(f'#{tc} {max(visited[K & 1])}')