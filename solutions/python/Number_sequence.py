
try:
    while(True):
        y=input()
        x=input()
        x=x+" "
        if y.isupper():
            z=y.lower()
        else:
             z=y.upper()
        count=0
        for i in range(len(x)-1):
            if x[i]==z or x[i]==y:
                count+=1
                if x[i+1]==y or x[i+1]==z:
                    pass
                else:
                    print(count,end="")
            else:
                print(x[i],end="")
                count=0
        else:
            print(x[len(x)-1])        
except:
    pass          
            

