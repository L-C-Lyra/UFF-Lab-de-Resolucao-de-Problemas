n = int(input())
test = 0

for _ in range(n):
    test += 1
    points = 0
    card_hand = list(map(int, input().split()))

    card_hand.sort()

    switch = True
    for x in card_hand:
        for y in card_hand:
            if x != y and card_hand.count(x) == 2 and card_hand.count(y) == 2 and switch:
                xp, yp = y, x
                points = (3 * xp) + (2 * yp) + 20
                switch = False
            if x != y and card_hand.count(x) == 3 and card_hand.count(y) == 2 and switch:
                points = x + 160
                switch = False
        if switch:
            if card_hand.count(x) == 2 and switch:
                points = x
                switch = False
            if card_hand.count(x) == 3 and switch:
                points = x + 140
                switch = False
            if card_hand.count(x) == 4 and switch:
                points = x + 180
                switch = False

    print(f'Teste {test}')
    print(points)
    if test != n:
        print()
