from _collections import  deque

for tc in range(1, int(input()) + 1):
    N, M, L = map(int, input().split())
    temp = list(map(int, input().split()))
    Q = deque()
    for n in range(N):
        Q.append(temp[n])
    for m in range(M):
        cmd = list(map(str, input().split()))
        if cmd[0] == 'I':
            Q.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == 'D':
            Q.remove(Q[int(cmd[1])])
        elif cmd[0] == 'C':
            Q[int(cmd[1])] = int(cmd[2])
    result = Q[L] if L < len(Q) else -1
    print(f'{tc} {result}')