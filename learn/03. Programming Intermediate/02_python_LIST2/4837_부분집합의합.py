# import sys
# sys.stdin = open("4837_부분집합의합.txt", "r")

T = int(input())
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
sub_A = []
len_A = len(A)

for i in range(1 << len_A):
    templist = []
    for j in range(len_A):
        if i & (1 << j):
            templist.append(A[j])
    sub_A.append(templist)

for tc in range(T):
    N, K = map(int, input().split())        # N: 부분집합 원소의 수, K: 집합의 합

    result = 0
    for i in sub_A:
        if len(i) == N:
            if sum(i) == K:
                result += 1

    print('#{} {}'.format(tc + 1, result))