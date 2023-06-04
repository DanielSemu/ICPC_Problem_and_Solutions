x=int(input())
for i in range(x) :
    y=input()
    sum=0
    for j in range(len(y)):
        if y[i]=='斤':
            yy=int(y[i-2])
            print(yy)
            sum+=yy*0.5
        elif y[i]=='两':
             sum+=int(y[i])*0.05
    print(sum)

