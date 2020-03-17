T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    node = []
    for e in range(0, E):
        node.append(list(map(int, input().split())))
    start, end = map(int, input().split())
    result = 0

    stack = [start]

    flag = 1
    while flag:
        if len(stack) == 0:
            flag = 0
            break

        now = stack.pop()

        for i in range(0, E):
            if node[i][0] == now:
                if node[i][1] == end:
                    result = 1
                    flag = 0
                    break
                else:
                    stack.append(node[i][1])

    print('#{} {}'.format(tc, result))