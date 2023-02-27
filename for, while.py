# n = int(input())
# eagle = 0
# tails = 0
# for i in range(n):
#     x = int(input())
#     if x == 0:
#         eagle += 1
#     else:
#         tails += 1
# if eagle > tails:
#     print(tails)
# else:
#     print(eagle)


# x = int(input())
# y = int(input())
# for i in range(x):
#     for j in range(y):
#         if x == i + j and y == i * j:
#             print(i,j)

n = int(input())
i = 0
while 2 ** i <= n:
    print(2 ** i)
    i += 1