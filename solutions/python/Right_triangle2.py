import math


while 1:
    ang,hyp=map(int,input().split())
    d=ang* math.pi/180
    side1=math.sin(d)*hyp
    side2=math.cos(d)*hyp
    print(round(side2, 5),round(side1, 5))

