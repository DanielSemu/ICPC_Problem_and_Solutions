x=int(input())
for i in range(x):
    num=1
    y=int(input())
    tot=1
    toto=1
    for j in range(y):
        n,m=map(int, input().split())
        toto*=(m+1)
        if n%2!=0:
            tot*=(m+1)
    print(toto-tot)
    