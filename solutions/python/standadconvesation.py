from posixpath import split


lis=[]
while 1:
    x=[list for x in input().split()]
    if x=='[-1]':
        break
    print(x)
    lis.append(x)



print(lis)