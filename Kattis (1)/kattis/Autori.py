x=input()
print(x[0],end="")
for i in range(len(x)):
    if x[i]=='-':
        print(x[i+1],end="")