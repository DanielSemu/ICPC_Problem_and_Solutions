x,y,z=map(int, input().split())
ls=[0,0,0,0]
ls[0]=y*z*4
ls[1]=(x-z)*y*4
ls[2]=(x-y)*z*4
ls[3]=(x-y)*(x-z)*4
ls=sorted(ls)
print(ls[3])
