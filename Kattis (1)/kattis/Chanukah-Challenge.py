x=int(input())
for i in range(x):
    y,n=map(int, input().split())
    print(y,end=" ")
    z=(n*(n+1)//2)+n
    print(z)
    