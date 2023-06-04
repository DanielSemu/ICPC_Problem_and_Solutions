#to check if there is a number x which is n=x^k is integer value example 16=2^4
# n,k=map(int, input().split())
# x=n**(1/k)
# if x == int(x):
#     print("Yes")
# else:
#     print(x)
#     print("No")
#BASE CHANGE IN PYTHON
DIGITS = '0123456789abcdef'
def convert_to_base(decimal_number, base):
    remainder_stack = []

    while decimal_number > 0:
        remainder = decimal_number % base
        remainder_stack.append(remainder)
        decimal_number = decimal_number // base

    new_digits = []
    while remainder_stack:
        new_digits.append(DIGITS[remainder_stack.pop()])

    return ''.join(new_digits)

x=int(input())
print(convert_to_base(x, 2))  # => '11001'
print(convert_to_base(x, 16))