n = int(input())
territories_sections = list(map(int, input().split()))
sections_size_half = (sum(territories_sections)) // 2
sections_sizes_sum = 0
switch = True

i = 0
while i <= n and switch:
    if sections_sizes_sum == sections_size_half:
        switch = False
    else:
        sections_sizes_sum += territories_sections[i]
        i += 1

print(i)
