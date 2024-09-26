n = int(input())
numbers_floor = list()
circled_numbers = 0
aux = 0

for _ in range(n):
    v_i = int(input())
    numbers_floor.append(v_i)

for i in range(n):
    if aux != numbers_floor[i]:
        circled_numbers += 1
        aux = numbers_floor[i]

print(circled_numbers)
