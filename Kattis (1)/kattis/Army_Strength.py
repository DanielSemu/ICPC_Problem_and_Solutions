from posixpath import split


x=int(input())
for i in range(x):
    x,y=map(int, input().split())
    ls1= list(map(int,input().split()))[:x]
    ls2= list(map(int,input().split()))[:y]
    l1=sorted(ls1)
    l2=sorted(ls2)
    if len(l1) < len(l2):
        for i in range(len(l1)):
            if l1[i] >= l2[i]:
                l2.remove(l2[i])
            else:
                l1.remove(l1[i])
    else:
        for i in range(len(l2)):
            if l2[i] <= l1[i]:
                l2.remove(l2[i])
            else:
                l1.remove(l1[i])
    if(len(l1)>len(l2)):
        print("Godzilla")
    elif(len(l1)<len(l2)):
        print("MechaGodzilla")
    else:
        print("uncertain")