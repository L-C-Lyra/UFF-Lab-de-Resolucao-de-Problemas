cards = list(map(int, input().split()))
output = ['C', 'D', 'N']
pos_output = None

if cards[0] < cards[1] < cards[2] < cards[3] < cards[4]:
    pos_output = 0
elif cards[0] > cards[1] > cards[2] > cards[3] > cards[4]:
    pos_output = 1
else:
    pos_output = 2

print(output[pos_output])
