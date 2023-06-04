def pfactor(num):
    c=2
    while (num>1):
        if( num%c ==0):
            print(c, end=" ")
            num=num/c
        else:
            c=c+1
    
while(True):
    x=int(input())
    if x== -1:
        break
    pfactor(x)
    print("")