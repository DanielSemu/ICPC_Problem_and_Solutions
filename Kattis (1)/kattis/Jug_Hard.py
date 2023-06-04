from math import gcd
t=int(input())
for i in range(t):
    x,y,z=map(int, input().split())
    gc=gcd(x,y)
    if z%gc ==0:
        print("Yes")
    else:
        print("No")