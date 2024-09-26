n = int(input())
test = 0

while n != 0:
    test += 1
    counters = [[0] * 10 for _ in range(6)]
    # counters = []
    # for _ in range(6):
    #     counters.append([0] * 10)

    for _ in range(n):
        line = input().split()
        line_mapping = []

        for i in range(5):
            line_mapping.append([int(line[i * 2]), int(line[i * 2 + 1])])
        #   line_mapping = input().split()
        #   a = [int(line_mapping[0]), int(line_mapping[1])]
        #   b = [int(line_mapping[2]), int(line_mapping[3])]
        #   c = [int(line_mapping[4]), int(line_mapping[5])]
        #   d = [int(line_mapping[6]), int(line_mapping[7])]
        #   e = [int(line_mapping[8]), int(line_mapping[9])]

        for i in range(6):
            actual_counter = counters[i]
            informed_letter = line[10 + i]
            pair = line_mapping[ord(informed_letter) - ord('A')]
            actual_counter[pair[0]] += 1
            actual_counter[pair[1]] += 1

    print(f'Teste {test}')

    for i in range(6):
        actual_counter = counters[i]
        most_informed = -1
        most_informed_letter = None
        for j in range(10):
            if actual_counter[j] > most_informed:
                most_informed = actual_counter[j]
                most_informed_letter = j
        print(most_informed_letter, end=' ')

    print()
    print()

    n = int(input())
