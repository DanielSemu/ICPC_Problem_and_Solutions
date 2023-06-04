x=input()
count=1
print(x[0])
for i in range(len(x)-1):
    if x[i]==x[i+1]:
        count+=1
print(len(x)-count+1)