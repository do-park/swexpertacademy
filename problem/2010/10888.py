from itertools import combinations


T = int(input())
for tc in range(T):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]
    stores = []
    customers = []
    for row in range(N):
        for col in range(N):
            if maps[row][col] > 1:
                stores.append((row, col))
            elif maps[row][col] == 1:
                customers.append((row, col))
    answer = 9876543210
    for i in range(1, len(stores) + 1):
        picked_store = list(combinations(stores, i))
        for j in range(len(picked_store)):
            result = 0
            for customer in customers:
                distance = 987654321
                for k in range(i):
                    distance = min(distance, abs(customer[0] - picked_store[j][k][0]) + abs(customer[1] - picked_store[j][k][1]))
                result += distance
            for k in range(i):
                result += maps[picked_store[j][k][0]][picked_store[j][k][1]]
            answer = min(answer, result)
    print(f'#{tc+1} {answer}')