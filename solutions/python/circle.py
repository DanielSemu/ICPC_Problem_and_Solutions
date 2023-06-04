import math
x=int(input())
ls=[int(ls) for ls in input().split()]
ls=sorted(ls)
len=len(ls)
val=pow(ls[0],2)
for i in range(1,len):
    val=pow(ls[i],2)-val
num=math.pi *val
print("{:.6f}".format(num))
