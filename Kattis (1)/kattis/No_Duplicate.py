from itertools import count


str=[str(i) for i in input().split()]
count=0
for i in range(len(str)):
    x=str.count(str[i])
    if x>1:
        print("no")
        count+=1
        break
if count==0:
    print("yes")
