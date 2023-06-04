for i in range(int(input())):
    l=list(map(int,input().split()))[:10]
    x=sum(l)//4
    c=x-l[0]-l[9]
    a=l[1]-c
    b=l[0]-a
    e=l[8]-c
    d=l[9]-e
    x = []
    x.append(a)
    x.append(b)
    x.append(c)
    x.append(d)
    x.append(e)
    x.sort()
    print("Case ",end='')
    print(i+1,end=': ')
    print(x[0],x[1],x[2],x[3],x[4])
    