n = int(input())
concept = ['E', 'D', 'C', 'B', 'A']
concept_pos = None

if n == 0:
    concept_pos = 0
if n >= 1 and n <= 35:
    concept_pos = 1
if n >= 36 and n <= 60:
    concept_pos = 2
if n >= 61 and n <= 85:
    concept_pos = 3
if n >= 86 and n <= 100:
    concept_pos = 4

print(concept[concept_pos])
