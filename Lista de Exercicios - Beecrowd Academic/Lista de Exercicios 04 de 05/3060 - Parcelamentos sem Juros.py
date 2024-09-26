v = int(input())
p = int(input())
list_parcels = list()

for _ in range(p):
    list_parcels.append(v // p)

rest = v % p
i = 0
while rest > 0:
    list_parcels[i] += 1
    rest -= 1
    i += 1

for parcels in list_parcels:
    print(parcels)
