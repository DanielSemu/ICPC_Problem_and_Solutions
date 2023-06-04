from platform import libc_ver
from re import T


n=int(input())
l=[]
isDublicated=False
isLenofN=False
isSorted=True
max='/'
for j in range(n):
    m=input()
    f=[]
    for i in m:
        if i in f:
            isDublicated=True
        f.append(i)
        if len(f)>n:
            isLenofN=True
    l.append(list(f))
z=[]
for k in range(len(l)):
    for m in range(len(l[k])):
        g=[]
        if m==0:
            z.append(l[m][k])
        if l[m][k] not in g:
            g.append(l[m][k])
        else:
            isDublicated=True
max='/'
for s in l[0]:
    if s>max:
        max=s
    else:
        isSorted=False
        break
max='/'
for t in z:
    if t>max:
        max=t
    else:
        isSorted:False
        break
if isDublicated or isLenofN:
    print('No')
elif not isSorted:
    print('Not Reduced')
else:
    print('Reduced')