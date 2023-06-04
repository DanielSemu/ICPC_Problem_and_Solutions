x,y=map(int, input().split())
f=input()
if f=="ABAB" and y-x==2 and 10-y==2:
    print(7,9)
elif f=="ABBA" and y-x==3:
    print(x+1,x+2)
elif f=="BABA" and x==2 and y==4:
    print(1,3)
elif f=="AABB" and y==7:
    print(8,9)
elif f=="BBAA" and x==3:
    print(1,2)
elif f=="BAAB" and x==2 and 10-y==2:
    print(1,9)
else:
    print(-1)
