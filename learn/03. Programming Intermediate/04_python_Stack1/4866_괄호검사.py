T = int(input())

for tc in range(1, T + 1):
    S = list(map(str, input()))
    stack = []

    result = 1
    for s in S:
        if s == '{' or s == '(':
            stack.append(s)

        elif s == '}':
            if len(stack) == 0:
                result = 0
                break
            if stack[-1] != '{':
                result = 0
                break
            else:
                stack.pop()

        elif s == ')':
            if len(stack) == 0:
                result = 0
                break

            if stack[-1] != '(':
                result = 0
                break
            else:
                stack.pop()

    if len(stack) != 0:
        result = 0

    print('#{} {}'.format(tc, result))