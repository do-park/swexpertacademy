T = int(input())

for tc in range(T):
    Sarr = [1 for _ in range(14)]
    Darr = [1 for _ in range(14)]
    Harr = [1 for _ in range(14)]
    Carr = [1 for _ in range(14)]


    str = input()
    cards = []
    for i in range(0, len(str), 3):
        cards.append(str[i:i+3])

    for card in cards:
            if 'S' in card:
                Sarr[int(card[1:3])] -= 1
            if 'D' in card:
                Darr[int(card[1:3])] -= 1
            if 'H' in card:
                Harr[int(card[1:3])] -= 1
            if 'C' in card:
                Carr[int(card[1:3])] -= 1

    if Sarr.count(-1) or Darr.count(-1) or Harr.count(-1) or Carr.count(-1):
        print('#{} ERROR'.format(tc + 1))
    else:
        print('#{} {} {} {} {}'.format(tc + 1, sum(Sarr) - 1, sum(Darr) - 1, sum(Harr) - 1, sum(Carr) - 1))