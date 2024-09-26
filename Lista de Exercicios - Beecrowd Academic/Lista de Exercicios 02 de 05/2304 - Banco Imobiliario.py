def payer(operation, current, rent):
    m, n = 1, 2
    if rent:
        m, n = 2, 3

    if operation[m] == 'D':
        current[0] -= int(operation[n])
    elif operation[m] == 'E':
        current[1] -= int(operation[n])
    elif operation[m] == 'F':
        current[2] -= int(operation[n])

    return current


def receiver(operation, current, rent):
    n = 2
    if rent:
        n = 3

    if operation[1] == 'D':
        current[0] += int(operation[n])
    elif operation[1] == 'E':
        current[1] += int(operation[n])
    elif operation[1] == 'F':
        current[2] += int(operation[n])

    return current


def main():
    i, o = map(int, input().split())
    money = list()
    for _ in range(3):
        money.append(i)

    for _ in range(o):
        operations = input().split()
        if operations[0] == 'C':
            money = payer(operations, money, False)
        elif operations[0] == 'V':
            money = receiver(operations, money, False)
        elif operations[0] == 'A':
            money = receiver(operations, money, True)
            money = payer(operations, money, True)

    print(f'{money[0]} {money[1]} {money[2]}')


if __name__ == '__main__':
    main()
