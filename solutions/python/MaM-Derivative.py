s=input()
li=list(map(str,s.split()))
m=""
count=0
for i in li[0]:
    if i.isdigit():
        m+=i
    if i.isalpha():
        count+=1
if count==0:
    print(0)
else:
    if count>0 and len(m)==0:
        if li[0][0]=="-":
         print(-1)
        else:
            print(1)
    else:
        if li[0][0]=="-":
            print("-"+m)
        else:
            print(m)
###########################
x=input()
li=list(map(str,x.split()))
num="-1234567890"
str=""
if x[0] not in num:
    print(1)
elif x[0]=="-" and x[1] not in num:
    print(-1)
else:
    for i in range(len(x)):
        if x[i] in num:
            str+=x[i]
        else:
            break
if str == li[0]:
    print(0)
else:
    print(str)