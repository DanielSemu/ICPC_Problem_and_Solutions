def reduce(n, d):
    def gcd(n, d):
        while d != 0:
            t = d
            d = n%d
            n = t
        return n
    assert d!=0
    assert isinstance(d, int)
    assert isinstance(n, int)
    gc=gcd(n,d)
    n//=gc
    d//=gc
    return n, d
x=int(input())
for i in range(x):
    lst = input().split()
    z,f=reduce(int(lst[0]),int(lst[2]))
    print(z,"/",f)