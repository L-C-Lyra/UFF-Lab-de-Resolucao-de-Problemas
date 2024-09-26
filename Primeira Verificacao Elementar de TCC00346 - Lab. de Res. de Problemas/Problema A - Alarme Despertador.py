times = list(map(int, input().split()))

while ((times[0] != 0) or (times[1] != 0)) and ((times[2] != 0) or (times[3] != 0)):
    if times[0] == 0:
        times[0] = 24
    if times[2] == 0:
        times[2] = 24

    if times[0] < times[2] and times[1] < times[3]:
        mins = ((times[2] - times[0]) * 60) + (times[3] - times[1])
    if times[0] < times[2] and times[1] == times[3]:
        mins = (times[2] - times[0]) * 60
    if times[0] < times[2] and times[1] > times[3]:
        mins = (60 - times[1]) + times[3]

    if times[0] == times[2] and times[1] < times[3]:
        mins = (times[3] - times[1])
    if times[0] == times[2] and times[1] == times[3]:
        mins = 1440
    if times[0] == times[2] and times[1] > times[3]:
        mins = 1440 - (times[1] - times[3])

    if times[0] > times[2] and times[1] < times[3]:
        mins = ((24 - (times[0] - times[2])) * 60) + (times[3] - times[1])
    if times[0] > times[2] and times[1] == times[3]:
        mins = (24 - (times[0] - times[2])) * 60
    if times[0] > times[2] and times[1] > times[3]:
        mins = ((24 - (times[0] - times[2])) * 60) - (times[1] - times[3])

    print(mins)

    times = list(map(int, input().split()))
