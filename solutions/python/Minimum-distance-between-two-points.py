while 1:
    x=int(input())
    if x== -1:
        break
    num=[int(i) for i in input().split()]
    num=sorted(num)
    min=1000000000
    for i in range(len(num)-1):
        if num[i+1] -num[i]<min:
            min=num[i+1] - num[i]
    print(min)
