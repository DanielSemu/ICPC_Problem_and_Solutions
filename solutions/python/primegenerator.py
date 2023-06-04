# works 10^5 in 1 sec
from math import sqrt


def isPrime(n):
    b = int(sqrt(n)+1)
    if n==1:
        return False
 
    for i in range(2,b):
        if n%i==0:
            return False
    return True

for _ in range(int(input())):
    x,y = map(int, input().split())
    
    for i in range(x,y+1):
        if isPrime(i):
            print(i,end=' ')
