T = int(input())

for tc in range(1, T + 1):
    S = list(map(str, input()))
    L = len(S)
    stack = []

    for l in range(0, L):
        if not stack or stack[-1] != S[l]:
            stack.append(S[l])
        else:
            stack.pop()

    print('#{} {}'.format(tc, len(stack)))