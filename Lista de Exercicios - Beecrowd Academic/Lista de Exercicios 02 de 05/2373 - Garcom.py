n = int(input())
broken_c = 0

for _ in range(n):
    l, c = map(int, input().split())

    if l > c:
        broken_c += c

print(broken_c)
