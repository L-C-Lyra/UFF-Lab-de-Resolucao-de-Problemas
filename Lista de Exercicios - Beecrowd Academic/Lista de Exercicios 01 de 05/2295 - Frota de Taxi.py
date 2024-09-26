a, g, r_a, r_g = map(float, input().split())
output = ['A', 'G']
output_pos = None

if (a / r_a) < (g / r_g):
    output_pos = 0
else:
    output_pos = 1

print(output[output_pos])
