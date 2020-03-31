for tc in range(1, int(input()) + 1):
    N = int(input())
    answer = -1
    for n in range(1, N + 1):
        result = n ** 3
        if result == N:
            answer = n
            break
        elif result > N:
            break
    print(f'#{tc} {answer}')