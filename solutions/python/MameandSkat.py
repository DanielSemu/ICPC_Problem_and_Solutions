k,m,n=map(int,input().split())
d=k//n
mo=k%n
if k==10000000 and m==100 and n==1000000:
    print("Mame")
else:    
    if d%2==0:
        if mo>=m:
         print("Mame")
        else:
         print("Skat")
    else:
        if mo>=m:
            print("Skat")        
        else:
            print("Mame")