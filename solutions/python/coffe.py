from math import floor


for _ in range(int(input())):
    c,p= map(int, input().split())
    name = {}
    sm = []
    me = []
    lg = []
    for i in range(c):
        n,s,m,l= map(str, input().split())
        s= int(s)
        m= int(m)
        l= int(l)
        name[n]= [s,m,l]
    for i in range(p):
        a,b,c = map(str, input().split())
        q=0
        if b == 'medium':
            q = name[c]
            q = q[1]
        elif b == 'small':
            q = name[c]
            q = q[0]
        elif b == 'large':
            q = name[c]
            q = q[2]
        dp = 100//p
        tc = q+dp
        if tc%5==1: 
            tc = tc-1
        elif tc%5==4:
            tc=tc+1
        else:
            tc= tc

        print(a,tc)