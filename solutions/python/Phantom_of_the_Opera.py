x=int(input())
for i in range(x):
    y,z=map(int,input().split())
    out=y-z
    if out<0:
        print(0)
    else:
        print(out)
