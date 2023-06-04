x = list(input().split())
len=len(x)
count=0
for i in range(len):
    for j in range(len):
        if x[i]!=x[j]:
            count+=1
       
            
if count>1:
    print("YES")

