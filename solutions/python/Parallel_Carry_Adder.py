for _ in range(int(input())):
    a,b=map(str,input().split())
    print(a,b)
    a=int(a,2)
    b=int(b,2)
    while 1:
        c=a^b
        d=(a&b)*2
        if d>=2**31:
            print('{0:031b}'.format(c),"overflow")
            break
        elif d==0:
            print('{0:031b}'.format(c),'{0:031b}'.format(d))
            break
        print('{0:031b}'.format(c),'{0:031b}'.format(d))
        a=c
        b=d
    print()