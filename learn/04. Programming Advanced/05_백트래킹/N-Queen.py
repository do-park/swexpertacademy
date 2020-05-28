def check(k):
    for i in range(k):   # 이전 행들을 검사함
        if col[k] == col[i] or abs(k-i) == abs(col[k]-col[i]): # 같은 열이거나 대각선이 같으면 (거리가 같으면)
            return False
    return True

def dfs(n, k):
    global count
    if k == N-1: #마지막 행까지 퀸을 놓으면 정답
        count += 1
    else:
        for i in range(N):
            col[k+1] = i  #다음 행에 차례대로 퀸을 놓아봄
            if check(k+1):
                dfs(n, k+1)

import sys
# sys.stdin = open("(2806)N-Queen_input.txt")
T = int(input())
for tc in range(T):
    N = int(input())
    col = [0] * N  # N-Queen에서 각 행에 하나의 퀸만 놓을 수 있음.
    count = 0
    for i in range(N):
        col[0] = i  #첫행에 들어갈 퀸을 하나씩 넣어봄
        dfs(N, 0)
    print("#{} {}".format(tc+1, count))
