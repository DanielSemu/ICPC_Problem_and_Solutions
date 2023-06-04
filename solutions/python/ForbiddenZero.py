x=int(input())
while 1:
    x+=1
    t=str(x)
    if "0" not in t:
        print(t)
        break
##################
# from math import gcd
# try:
#     while True:
        
#         a,b,c=map(int,input().split())
#         d=(a*b)
#         e=abs(b-c)
#         f=gcd(d,e)
#         d=d//f
#         e=e//f
#         print(f"{d}/{e}")
# except:
#     pass 