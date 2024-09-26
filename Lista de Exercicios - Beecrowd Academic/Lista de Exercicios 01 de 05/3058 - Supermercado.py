lowest_price = float('inf')
n = int(input())

for _ in range(n):
    p, g = input().split()
    p = float(p)
    g = int(g)

    price_per_kg = p * (1000 / g)

    if price_per_kg < lowest_price:
        lowest_price = price_per_kg

print(f'{lowest_price:.2f}')
