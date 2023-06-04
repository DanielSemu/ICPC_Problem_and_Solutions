
import math
x=int(input())
sum=0
for i in range(x):
    y=int(input())
    for j in range(y):
        x,y=map(int, input().split())
        d=math.sqrt((x*x)+(y*y))
        if d <= 20 :
            sum+=10
        elif d <=40:
            sum+=9
        elif  d <= 60:
            sum+=8
        elif  d <= 80:
            sum+=7
        elif d <= 100:
            sum+=6
        elif d <= 120:
            sum+=5
        elif  d <= 140:
            sum+=4
        elif d <= 160:
            sum+=3
        elif  d <=180:
            sum+=2
        elif d <=200:
            sum+=1
        else:
            sum+=0
    print(sum)
