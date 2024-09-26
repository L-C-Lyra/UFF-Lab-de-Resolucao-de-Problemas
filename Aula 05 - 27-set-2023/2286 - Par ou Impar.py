n = int(input())
test = 0

while n != 0:
    test += 1
    player_pair = input()
    player_unpair = input()
    print(f'Teste {test}')
    for _ in range(n):
        value_pair, value_unpair = map(int, input().split())
        print(player_pair if (value_pair + value_unpair) % 2 == 0 else player_unpair)
        # if (value_pair + value_unpair) % 2 == 0:
        # 	print(player_pair)
        # else:
        # 	print(player_unpair)
    n = int(input())
    print()
