l = int(input())
c = int(input())

if l % 2 == 0:
    if c % 2 != 0:
        print(0)
    else:
        print(1)
else:
    if c % 2 != 0:
        print(1)
    else:
        print(0)

# if l & 1 == 0:
#     if c & 1 == 0:
#         print(1)
#     else:
#         print(0)
# else:
#     if c & 1 == 0:
#         print(0)
#     else:
#         print(1)
