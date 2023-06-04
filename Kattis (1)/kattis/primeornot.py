from math import sqrt


try: 
    while True:
        x=int(input())
        count=0
        for i in range(2,int(sqrt(x))+1):
            if x%i==0:
                print("Not Prime")
                count=0
                break
            else:
                count+=1
        if count!=0:
            print("Prime")
     
            
except:
    pass