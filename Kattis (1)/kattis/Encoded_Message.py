from math import sqrt


x=input()
d=int(sqrt(len(x)))
print(d)
arr=[][10000]
f=0
for i in range(d):
    for j in range(d):
        arr[i][j]=x[f]
        f+=1
for i in range(d-1,0):
    for j in range(d-1):
        print(x[i][j],end="")
 