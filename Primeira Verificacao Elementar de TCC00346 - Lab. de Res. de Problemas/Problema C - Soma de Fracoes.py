nums = list(map(int, input().split()))

if nums[1] == nums[3]:
    divd = (nums[0] + nums[2])
    divs = nums[1]
elif nums[1] != nums[3]:
    for div in range(2, nums[1] + 1):
        while nums[0] % div == 0 and nums[1] % div == 0:
            nums[0] = int(nums[0] / div)
            nums[1] = int(nums[1] / div)

    for div in range(2, nums[3] + 1):
        while nums[2] % div == 0 and nums[3] % div == 0:
            nums[2] = int(nums[2] / div)
            nums[3] = int(nums[3] / div)

    divd = (nums[0] * nums[3]) + (nums[1] * nums[2])
    divs = (nums[1] * nums[3])

for div in range(2, divs + 1):
    while divd % div == 0 and divs % div == 0:
        divd = int(divd / div)
        divs = int(divs / div)

print(f'{divd} {divs}')
