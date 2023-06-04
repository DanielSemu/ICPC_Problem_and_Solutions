x=input()
ls=[1,2,3]
temp=0
for i in range(len(x)):
    if x[i]=='A':
        ls[0],ls[1]=ls[1],ls[0]
    elif x[i]=='B':
        ls[1],ls[2]=ls[2],ls[1]
        
    elif x[i]=='C':
        ls[0],ls[2]=ls[2],ls[0]
for i in range(3):
    if ls[i]==1:
        print(i+1)
        break