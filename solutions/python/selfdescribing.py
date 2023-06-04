x=int(input())
for i  in range(x):
    y=input()
    count=0
    for i in range(len(y)):
        if y.count(str(i))==int(y[i]):
            count+=1
        else:
            count=0
    if count>0:
        print("self-describing")
    else:
        print("not self-describing")
