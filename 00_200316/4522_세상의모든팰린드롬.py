for tc in range(1, int(input()) + 1):
    flag = ['Not exist', 'Exist']
    f = 1
    string = list(map(str, input()))
    for i in range(0, len(string) // 2):
        if string[i] != string[len(string) - i - 1]:
            if string[i] == '?' or string[len(string) - i - 1] == '?':
                continue
            else:
                f = 0
                break
    print(f'#{tc} {flag[f]}')