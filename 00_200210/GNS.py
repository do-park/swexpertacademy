import sys
sys.stdin = open("GNS.txt", "r")

T = int(input())
for tc in range(1, T+1):
    num = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    Base = {'ZRO': 0, 'ONE': 0, 'TWO': 0, 'THR': 0, 'FOR': 0, 'FIV': 0, 'SIX': 0, 'SVN': 0, 'EGT': 0, 'NIN': 0}
    tc_list = list(input().split())
    Data = list(input().split())

    for i in Data:
        Base[i] += 1

    print('#{}'.format(tc))
    for i in range(10):
        print('{} '.format(num[i]) * Base[num[i]], end='')
    print()
