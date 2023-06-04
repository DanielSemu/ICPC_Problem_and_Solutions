import math
x=int(input())
for i in range(x):
    y=int(input())
    z=str(math.factorial(y))
    print(z)
    print(len(z))
# Python program to find the factorial of a number provided by the user
# using recursion

# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return (x * factorial(x-1))
# x=int(input())
# for i in range(x):
#     num = int(input())
#     if num==0:
#         print(1)
#     else:
#          result = str(factorial(num))
#          print(result)
#          print(len(result))