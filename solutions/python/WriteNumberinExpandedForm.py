num=int(input())
result = []
for index, digit in enumerate(str(num)[::-1]):
    if int(digit) != 0:
        result.append(digit + ('0' * index))
print( ' + '.join(result[::-1]))