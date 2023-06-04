x=int(input())
for j in range(x):
    numbers = [int(num) for num in input().split()]
    count=0
    for i in range(4):
        if numbers[i]<numbers[i+1] and numbers[i]+1 == numbers[i+1]:
            count+=1
            continue
        else:
            print("N")
            count=0
            break
    if count>0:
        print("Y")