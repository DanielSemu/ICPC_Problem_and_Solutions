from math import sqrt
while 1:
    x=int((input()))
    if x==-1:
        break
    y=int(sqrt(x))
    count=-1
    if x<4:
        count==-1  
    else:
        for i in range(2,y+1):
            if x%i==0:
                print(x," is is COMPOSITE TT")
                count+=1
                break
            else:
                count+=0 
    if(count==-1):
        print(x," is PRIME!!")  




    

    