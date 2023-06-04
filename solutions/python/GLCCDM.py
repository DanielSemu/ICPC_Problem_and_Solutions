from math import gcd
while(True):
    x=input()
    if x=='-1':
        break
    y,z= map(int, x.split())
    yy=gcd(y,z)
    zz=(y*z)//yy  #double slash to print intiger value only
    print(yy , " " , zz)
