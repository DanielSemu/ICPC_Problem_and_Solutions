from math import sqrt
def isPrime(n):
    b = int(sqrt(n)+1)
    if n==1:
        return False
 
    for i in range(2,b):
        if n%i==0:
            return False
    return True

x=int(input())
for i in range(x):
    y=int(input())
    count=0
    ls=[]
    for j in range(1,y//2+1):
        if isPrime(j) and isPrime(y-j):
            count+=1
            ls.append(j)
            ls.append(y-j)
    print(y,"has",count," representation(s)")
    for k in range(0,len(ls),2):
        print(ls[k],end="")
        print("+",end="")
        print(ls[k+1])
