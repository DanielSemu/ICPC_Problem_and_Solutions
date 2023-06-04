from ntpath import join


x= input()
k =[]
for i in x:
    if i.isupper():
        i = i.lower()
        k.append(i)

print("".join(k))
