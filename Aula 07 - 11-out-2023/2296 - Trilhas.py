import sys

lowest_less_effort = sys.maxsize
lowest_less_effort_id = None

n = int(input())

for id in range(1, n + 1):
    m, *h = map(int, input().split())
    # values = list(map(int, input().split()))
    # m = values[0]
    # h = []
    # for i in range(1, m + 1):
    # 	h.append(values[i])

    # right_effort = 0
    # for i in range(m - 1):
    # 	if h[i] < h[i + 1]:
    # 		right_effort += (h[i + 1] - h[i])
    #
    # left_effort = 0
    # for i in range(m - 1, 0, -1):
    # 	if h[i] < h[i - 1]:
    # 		left_effort += (h[i - 1] - h[i])

    right_effort = 0
    left_effort = 0
    for i in range(m - 1):
        if h[i] < h[i + 1]:
            right_effort += (h[i + 1] - h[i])
        elif h[i] > h[i + 1]:
            left_effort += (h[i] - h[i + 1])

    less_effort = min(right_effort, left_effort)

    if less_effort < lowest_less_effort:
        lowest_less_effort = less_effort
        lowest_less_effort_id = id

print(lowest_less_effort_id)
