test=int(input())
for i in range(test):
    input()
    x=int(input())
    sum=0
    for c in range(x):
        sum=sum+ int(input())

    if sum % x==0:
            print("YES")
    else:
            print("NO")
