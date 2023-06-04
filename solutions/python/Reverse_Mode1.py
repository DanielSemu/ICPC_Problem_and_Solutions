x=int(input())
numbers = [int(num) for num in input().split()]
dif=numbers[1]-numbers[0]
print(dif*x+numbers[0])
