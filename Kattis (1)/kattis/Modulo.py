lst=[]
for i in range(10):
    x=int(input())
    lst.append(x)
lst2=[]
for i in range(10):
    y=(lst[i]%42)
    lst2.append(y)
lst3=[]
for i in range(10):
    if lst2[i] in lst3:
        continue
    else:
        lst3.append(lst2[i])
    
print(len(lst3))