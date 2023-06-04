x=int(input())
str=""
for i in range(x):
    y=input()
    str=str+y
count=0
for i in range(x-1):
    if str[i]==str[i+1]:
        count+=1
print(count)
