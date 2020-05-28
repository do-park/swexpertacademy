# SWEA 5252 공통 단어 탐색

for tc in range(1, int(input()) + 1):
    A, B = map(int, input().split())
    AS = set()
    for a in range(A):
        AS.add(input())
    result = 0
    for b in range(B):
        pattern = input()
        if pattern in AS:
            result += 1
    print(f'#{tc} {result}')