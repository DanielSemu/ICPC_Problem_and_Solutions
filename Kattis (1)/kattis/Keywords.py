t=int(input())
lst=[]
for i in range(t):
    x=input()
    if "-" in x:
        x=x.replace("-","\t")
    x=x.lower()
    if x in lst:
        continue
    else:
        lst.append(x)

print(len(lst))