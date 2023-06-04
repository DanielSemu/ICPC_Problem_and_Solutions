x=int(input())
ls=[]
for i in range(x):
    y=input()
    ls.append(y)
    le=len(ls)
    count=0
    for j in range(le):
        if y==ls[j]:
            count+=1
    if count==1:
        print("Customer #",end="")
        print(i+1,end="")
        print(":Welcome to Moe's!!!")
    else:
        print("Customer #",end="")
        print(i+1,end="")
        print(":**continue working**")

