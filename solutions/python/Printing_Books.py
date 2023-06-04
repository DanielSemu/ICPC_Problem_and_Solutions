x,y=map(int,input().split())
page=0
i=0
count=0
while 1:
    z=str(y)
    page+=len(z)
    y+=1
    i+=1
    if page==x:
        count+=1
        break
    elif page<x:
        continue
    elif page>x:
        break
if count>0:
    print(i)
else:
    print(-1)