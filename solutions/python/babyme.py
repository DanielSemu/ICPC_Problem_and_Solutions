x=int(input())
for i in range(x):
    lst = list( input().split())
    if(len(lst)==2):
        e=0.5*int(lst[0])
        print("Case",i+1,end="")
        print(":",end=" ")
        print( '{:,g}'.format( e))
    else:
        d=0.5* int(lst[0])
        f=0.05* int(lst[2])
        z=f+d
        print("Case",i+1,end="")
        print(":",end=" ")
        print( '{:,g}'.format( z))