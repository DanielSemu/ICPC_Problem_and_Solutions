x = [i for i in input().split()]

print(x)
co = []
for i in x:
    co.append(x.count(i))
co.sort()
print(co)
if co[len(co)-1]>1:
    print(0)
else:
    print(1)
