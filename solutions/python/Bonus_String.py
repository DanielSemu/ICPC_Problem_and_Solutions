lst=[]
for i in range(3):
    lst.append(input())
for i in range(3):
    for j in range(i,3):
        if len(lst[i]) > len(lst[j]):
            temp=lst[i]
            lst[i]=lst[j]
            lst[j]=temp
for i in range(2):
    if len(lst[i])==len(lst[i+1]):
        if lst[i]>lst[i+1]:
            lst[i],lst[i+1]=lst[i+1] ,lst[i]
for i in range(3):
    print(lst[i])


