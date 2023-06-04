x=int(input())
z="Simon says"
zz=len(z)
for i in range(x): 
    d=""  
    s=input()
    xx=len(s)
    if xx>zz:
        for i in range(zz):
            if z[i]==s[i]:
                d=d+s[i]
        if d == z:
            for i in range(11, xx):
                print(s[i],end="")
            print("")
        

