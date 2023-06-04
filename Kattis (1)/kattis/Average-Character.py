x=input()
z=len(x)
x=x+" "
sum=0
for i in range(z):
    sum+=ord(x[i])
print(chr(int(sum/z)))

