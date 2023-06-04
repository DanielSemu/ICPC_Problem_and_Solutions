a= input()
v= ['a','e', 'i', 'o', 'u']
vow=[]
cons= []
for i in a:
    if i in v:
        vow.append(i)
    else:
        cons.append(i)
b = sorted(vow, reverse=True)
c= sorted(cons, reverse=True) 
for i in a:
    if i in v:
        print(b[len(b)-1], end='')
        b.pop()
    else:
        print(c[len(c)-1], end='')
        c.pop()
print()
####################
x=input()
vow=[]
cons=[]
vowel="AEIOUaeiou"
for i in range(len(x)):
    if x[i] in vowel:
        vow.append(x[i])
    else:
        cons.append(x[i])
v=sorted(vow,reverse=True)
c=sorted(cons,reverse=True)
for i in range(len(x)):
    if x[i] in vowel:
        print(v.pop(),end="")
    else:
        print(c.pop(),end="")