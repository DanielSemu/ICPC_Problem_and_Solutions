t=int(input())
for i in range(t):
    x,y,z=map(int, input().split())
    if x+y==z or x*y==z or abs(x-y)==z or x/y==z or y/x==z:
        print("Possible")
    else:
        print("Impossible")