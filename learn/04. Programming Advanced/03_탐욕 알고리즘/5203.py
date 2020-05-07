# SWEA 5203 베이비진 게임

def babygin(player):
    for i in range(10):
        if player[i] == 3:
            return True
        if i + 3 <= 10 and player[i] and player[i + 1] and player[i + 2]:
            return True

for tc in range(1, int(input()) + 1):
    cards = list(map(int, input().split()))
    player1 = [0] * 10
    player2 = [0] * 10
    winner = 0
    for i in range(12):
        if i & 1:
            player2[cards[i]] += 1
            if i > 5:
                if babygin(player2):
                    winner = 2
                    break
        else:
            player1[cards[i]] += 1
            if i > 5:
                if babygin(player1):
                    winner = 1
                    break
    print(f'#{tc} {winner}')