T = int(input())

for tc in range(T):
    str = input()
    length = len(str)

    for i in range(0, 5):
        if i == 0 or i == 4:
            temp = '..'+'#...'*(length)
            print(temp[:-1])
        elif i == 1 or i == 3:
            temp = '.#'*(length * 2) + '.'
            print(temp)
        else:
            temp = ''
            for s in str:
                temp += "#.{}.".format(s)
            temp += '#'
            print(temp)