from math import gcd

x=int(input())
for i in range(x):
    if x==0:
        break
    a,b,c=[int(i) for i in input().split()]
    if c%gcd(a,b)==0:
        print("Case" ,i+1, "Yes")
    else:
         print("Case" ,i+1, "No")
    