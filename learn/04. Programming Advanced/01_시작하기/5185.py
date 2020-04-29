# SWEA 5185 이진수

hex = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
for tc in range(1, int(input()) + 1):
    N, hexa = map(str, input().split())
    hexa = list(hexa)
    result = ''
    for n in range(int(N)):
        temp = ''
        if hexa[n] in hex:
            hexa[n] = hex[hexa[n]]
        for i in range(3, -1, -1):
            if int(hexa[n]) & 2 ** i:
                temp += '1'
            else:
                temp += '0'
        result += temp
    print(f'#{tc} {result}')