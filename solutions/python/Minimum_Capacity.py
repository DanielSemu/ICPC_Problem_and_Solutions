a,b,c=map(int ,input().split())
if c<a:
    print(c)
elif c>b:
    print(c)
else:
    print((b+c)-((b+c)%c))