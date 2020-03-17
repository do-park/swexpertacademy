T = int(input())
for tc in range(1, T + 1):
    s = list(map(str, input()))
    H = int(input())
    l = [0] * (len(s) + 1)
    temp = list(map(int, input().split()))
    for h in range(H):
        l[temp[h]] += 1

    for i in range(len(l)-1, -1, -1):
        while l[i]:
            s.insert(i, '-')
            l[i] -= 1
    print(f'#{tc} {"".join(s)}')