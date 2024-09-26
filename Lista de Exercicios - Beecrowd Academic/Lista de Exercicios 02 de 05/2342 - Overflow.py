n = int(input())
p, c, q = input().split()
p, q = int(p), int(q)
output = ['OK', 'OVERFLOW']
pos_output = 0

if c == '+':
    if p + q > n:
        pos_output = 1
elif c == '*':
    if p * q > n:
        pos_output = 1

print(output[pos_output])
