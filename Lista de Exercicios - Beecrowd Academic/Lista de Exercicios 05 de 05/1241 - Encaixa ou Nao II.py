n = int(input())

for _ in range(n):
    a, b = input().split()

    if len(b) > len(a):
        print('nao encaixa')
    else:
        switch = True
        i, j = len(a) - 1, len(b) - 1
        while switch and (i >= 0 and j >= 0):
            if a[i] != b[j]:
                switch = False
            i -= 1
            j -= 1

        print('encaixa' if switch else 'nao encaixa')
