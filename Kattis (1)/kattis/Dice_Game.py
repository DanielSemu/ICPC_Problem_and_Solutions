for i in range(1,2):
    x,y,z,v=map(int,input().split())
    x1,x2,y1,y2=map(int,input().split())

sum1=(x+y)/2. + (z+v)/2.
sum2=(x1+x2)/2. + (y1+y2)/2.
if(sum1>sum2):
    print("Gunnar")
elif(sum1<sum2):
    print("Emma")
else:
    print("Tie")
