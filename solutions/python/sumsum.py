x=input()
numbers = [int(num) for num in input().split()]
sum=0
for i in range(len(numbers)):
    sum=sum+numbers[i]
print(sum)