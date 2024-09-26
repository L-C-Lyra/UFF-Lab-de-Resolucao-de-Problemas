# Ler os Valores da Lista 1

# Calcular a Lista Acumulada A

# Para Cada Intervalo com Ínicio na Posição i e Término j faça
    # Calcule o Somatório no Intervalo usando a Lista Acumulada
    # Mostre o Resultado Calculado

def accumulated_list(list_n):
    acc_list_n = list()
    sum_values = 0
    for i in range(len(list_n)):
        sum_values += list_n[i]
        acc_list_n.append(sum_values)
    return acc_list_n


def sum_interval(acc_list_n, i, j):
    if i == 0:
        return acc_list_n[j]
    else:
        return acc_list_n[j] - acc_list_n[i - 1]


def main():
    list_a = list(map(int, input().split()))
    acc_list_a = accumulated_list(list_a)

    i, j = map(int, input().split())
    while i != -1 or j != -1:
        sum_acc_list_a = sum_interval(acc_list_a, i, j)
        print(sum_acc_list_a)
        i, j = map(int, input().split())


if __name__ == "__main__":
    main()
