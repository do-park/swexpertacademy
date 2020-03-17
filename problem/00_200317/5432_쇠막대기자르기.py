for tc in range(1, int(input()) + 1):
    pipe = list(map(str, input()))
    stack = []
    result = 0
    for p in range(0, len(pipe)):
        if pipe[p] == '(':
            stack.append(1)
        else:
            stack.pop()
            if pipe[p - 1] == '(':
                result += len(stack)
            else:
                result += 1
    print(f'#{tc} {result}')