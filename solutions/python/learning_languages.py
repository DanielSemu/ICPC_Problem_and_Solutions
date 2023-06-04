for _ in range(int(input())):
    string=input()
    a,b=map(str,input().split())
    if (a not in string) or (b not  in string[string.index(a)+len(a):]):
        print(0)
    else:
        c=string.index(a)
        d=string.index(b)+len(b)
        print(len(string[c:d]))