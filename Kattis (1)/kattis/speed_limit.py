while 1:
    x=int(input())
    if x==-1:
        break
    l1=[]
    l2=[]
    for i in range(x):
        a,b=map(int , input().split())
        l1.append(a)
        l2.append(b)
    sum=0
    xx=l2[0]
    for i in range(x):
       sum+= l1[i] * xx
       if i == x-1:
        break
       xx=l2[i+1]-l2[i]
    print(sum,"miles")
        