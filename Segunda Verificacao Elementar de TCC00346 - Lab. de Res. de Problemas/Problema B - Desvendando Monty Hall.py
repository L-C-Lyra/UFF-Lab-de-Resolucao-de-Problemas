n = int(input())
win_a_car_count = 0

for _ in range(n):
    chosen_door = int(input())

    if chosen_door != 1:
        win_a_car_count += 1

print(win_a_car_count)
