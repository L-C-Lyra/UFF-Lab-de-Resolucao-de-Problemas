l, c, m, n = map(int, input().split())
plantation = list()
biggest_sum_daisies = float('-inf')

for _ in range(l):
    plantation_row = list(map(int, input().split()))
    plantation.append(plantation_row)

for i in range(0, l, m):
    for j in range(0, c, n):
        sum_daisies = 0
        for sum_i in range(i, m + i, 1):
            for sum_j in range(j, n + j, 1):
                sum_daisies += plantation[sum_i][sum_j]
        if sum_daisies > biggest_sum_daisies:
            biggest_sum_daisies = sum_daisies

print(biggest_sum_daisies)
