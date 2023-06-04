for i in range(int(input())):
    a,b,c=map(int,input().split())
    if a==b and b==c:
        print("1",end=' ')
        print("1",end=' ')
        print("1")
        
    else:
        m=max(a,b)
        m1=max(m,c)
        if a==m1:
            a=0
            b=m1-b+1
            c=m1-c+1
        elif b==m1:
            a=m1-a+1
            b=0
            c=m1-c+1
        else:
            a=m1-a+1
            b=m1-b+1
            c=0
        print(a,end=' ')
        print(b,end=' ')
        print(c)