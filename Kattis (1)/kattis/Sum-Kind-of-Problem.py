x= int(input())
for i in range(x):
    y,z=map(int, input().split())
    sum1=z*(z+1)//2
    sum2=z**2
    sum3=z*(z+1)
    
    print(y,end=" ")
    print(sum1,end=" ")
    print(sum2, end=" ")
    print(sum3)