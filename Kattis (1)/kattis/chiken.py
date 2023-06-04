x,y=map(int,input().split())
z=y-x
if z>0:
    if z==1:
        print("Dr. Chaz will have ", z ," piece of chicken left over!")
    else:
        print("Dr. Chaz will have ", z ," pieces of chicken left over!")
    
else:
    if z==-1:
        print("Dr. Chaz needs ",abs(z)," more piece of chicken!")
    else:
        print("Dr. Chaz needs ",abs(z)," more pieces of chicken!")
    
