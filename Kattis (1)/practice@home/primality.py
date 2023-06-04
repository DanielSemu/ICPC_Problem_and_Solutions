from math import sqrt
def isprime(n):
    if n==2:
        return True
    if n==1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True
while 1:
    x=int(input())
    if x==-1:
        break
    if isprime(x):
        print("Prime")
    else:
        print("Not prime")