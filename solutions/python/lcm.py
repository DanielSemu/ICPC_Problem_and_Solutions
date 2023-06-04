from math import gcd, lcm
a = 0
while(True):

    a,b,c = [int(i) for i  in input().split()]
    if a== -1:
        break
    d = lcm(a,lcm(b,c))
    print(d)
    

