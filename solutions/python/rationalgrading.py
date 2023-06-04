while 1:
    ival,v= map(str,input().split())
    if ival=='0' and v=='0':
            break
    num=0
    v= int(v)
    if ival[1]=='X':
        num = int(ival,16)
    elif ival[0]=='0':
        num = int(ival,8)
    else:
        num= int(ival)
    co=0
    for i in range(v):
        a,b= map(str,input().split())
        b= int(b)
        if a == '++i':
            num+=1
            if num==b:
                co+=1       
            else:
                num = b      
        if a== 'i++':
            if num==b:
                co+=1
                num+=1    
            else:
                num = b
        if a=='--i':
            num-=1
            if num == b:
                co+=1   
            else:
                num = b
        if a=='i--':
            if num==b:
                co+=1
                num-=1   
            else:
                num = b
        if a=='i':
            if num==b:
                co+=1
            else:
                num = b
    print(co)