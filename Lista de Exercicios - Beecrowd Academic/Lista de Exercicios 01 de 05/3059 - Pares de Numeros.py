n, i, f = map(int, input().split())
vector = list(map(int, input().split()))
sums_i_f = 0

for j in range(n):
    for k in range(j, n - 1):
        if i <= (vector[j] + vector[k + 1]) <= f:
            sums_i_f += 1

print(sums_i_f)
