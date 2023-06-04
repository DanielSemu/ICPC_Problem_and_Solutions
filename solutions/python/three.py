from math import sqrt
def primeFact(n):
    b = int(sqrt(n)+1)
    for i in range(2,b):   
        if n%i==0:       
            while n%i==0:               
                s.append(i)
                n//=i                
    if n>1:
        s.append(n)
    
while 1:
    x=int(input())
    if x== -1:
        break
    s = []
    primeFact(x)
    s.sort()
    count=0
    for i in s:
        if(s[i]%10!=3):
            count+=1
            break
    if(count ==1):
        print(x,"NO")
    else:
        print(x," YES ")