# x=int(input())
# for i in range(x):
#     xx=input()
#     count=0
#     for i in range(len(xx)):
#         if xx[i]=='D':
#             break
#         else:
#             count+=1
#     print(count)
#the walking adam check it

n=int(input())

for j in range(n):
    c=0
    s=input()
    a=len(s)
    for i in range(a):
        if s[i]=='U':
            c=c+1
            if i==a-1:
                print(c)
                break
        else:
            print(c)
            break
