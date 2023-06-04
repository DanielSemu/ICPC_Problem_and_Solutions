x=int(input())
for i in range(x):
    lst=[str(i) for i in input().split() ]
    lst2=[]
    while(1):
        word=input()
        if word =="what does the fox say?":
            break
        lst1=word.split(" ")
        lst2.append(lst1[2])
    for i in range(len(lst)):
        if lst[i] in lst2:
            continue
        else:
            print(lst[i],end=" ")