# x,y=map(int,input().split())
# if y<= x//2:
#     print(x//2 + y)
# else:
#     print(y-(x//2))
x,y=map(int, input().split())
n=x//2
print((n+y)%x)