j=1
while 1:
    x=int(input())
    if x==0:
        break
    str=[]
    for i in range(x):
        str.append(input())
    print("Case",j,end="")
    print(":")
    print("#include<string.h>\n#include<stdio.h>\nint main(){")
    for i in range(x):
        if '"' in str[i]:
            data=str[i]
            data = data.rstrip(data[-1])
            print("printf(",end="")
            print('"',end="")
            print('\\',end="")
            print(data,end="")
            print(r"\"",end="")
            print(r'\n");')
        else:
            print('printf("',end="")
            print(str[i],end="")
            print(r'\n");')
    print(r'printf("\n");')
    print("return 0;")
    print("}")
    j+=1
    ################################
    from dataclasses import replace


n=int(input())
list1=[]
list2=[]
t=1
while(n!=0):
    for i in range(0,n):
        k=input()
        if '\\' in k:
            k=k.replace('\\','\\\\')
        if '\"' in k:
            k=k.replace('\"','\\"')
        list2.append(k)
    print("Case {}:".format(t))
    print("#include<string.h>")
    print("#include<stdio.h>")
    print("int main(){")
    for i in range(0,n):
        print("printf(""\"{}\\n\");".format(list2[i]))
    print("printf(\"\\n\");")
    print("return 0;")
    print("}")
    t=t+1
    n=int(input())
    list2=[]
        