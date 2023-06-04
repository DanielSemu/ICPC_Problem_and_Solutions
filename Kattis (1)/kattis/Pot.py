num=int(input())
sum=0
for i in range(num):
    x=int(input())
    x1=x%10
    x2=x//10
    sum+=pow(x2,x1)
print(sum)