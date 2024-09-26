banknotes = [50, 10, 5, 1]
v = int(input())
test = 0

while v != 0:
    test += 1
    bits = list()

    aux = 0
    for m in banknotes:
        bits.append(v // m)
        if bits[aux] > 0:
            v %= m
        aux += 1

    print(f'Teste {test}')
    for m in range(3):
        print(bits[m], end=' ')
    print(bits[3])

    print()

    v = int(input())
