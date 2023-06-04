# Python program to print prime factors

import math

def primeFactors(n):
    num=n
    nos = []
    while n % 2 == 0:
        print(n," NO")
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):

        while n % i == 0:
            nos.append(i)
            n = n // i
    if n > 2:
        nos.append(n)
    l = len(nos)
    count=0
    for i in range(l):
        if(nos[i]%10 !=3):
            # print(nos[i])
            print(num, " NO")
            count=0
            break
        else:
            count+=1
    if count>=1:
        print(num, " YES")

while 1:
    n = int(input())
    if n==-1:
        break
    if n==1:
        print(n," NO")
    else:
        primeFactors(n)


