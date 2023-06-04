x,y=map(int,input().split())
t=int(input())
li=[]
mi=[]
for i in range(t):
    xi,yi=map(int,input().split())
    li.append((x-xi)**2+(y-yi)**2)
    mi.append((xi,yi))
print(mi[li.index(min(li))])
#////////////
from math import sqrt
x,y = map(int, input().split())
t = int(input())
dx = []
dy =[]
mini=100000
ind = 0
for i in range(t):
    a,b= map(int, input().split())
    dx.append(a)
    dy.append(b)
    d = sqrt(pow(x-a,2)+pow(y-b,2))
    if d<mini:
        mini = d
        ind = i

print('('+str(dx[ind])+', '+str(dy[ind])+')')