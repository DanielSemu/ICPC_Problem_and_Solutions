from fractions import Fraction
import math
try:
    while 1:
        AB,AC,BD=map(int,input().split())
        dif1=BD-AC
        tet=math.atan(AB/dif1)
        TB=math.tan(tet)*BD
        ou=Fraction(TB-AB).limit_denominator()
        out=str(ou)
        if "/" in out:
            print(out)
        else:
            print(ou,end="")
            print("/1")
except:
    pass
################
# from math import gcd
# def reduceFraction(x, y):
#     d = gcd(x, y);
#     x = x // d;
#     y = y // d;
#     print(f'{x}/{y}');
# try:
#      while 1:
#             x, y, z = map(int, input().split(' '))
#             n1=x*y
#             n2=z-y
#             reduceFraction(n1, n2);
# except :
#     pass