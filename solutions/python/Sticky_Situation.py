from itertools import count


x=input()
numbers = [int(num) for num in input().split()]
numbers=sorted(numbers)
count=0
for i in range(len(numbers)-2):
    if numbers[i]+numbers[i+1]>numbers[i+2]:
        count+=1
        break
if count==0:
    print("impossible")
else:
   print("possible")