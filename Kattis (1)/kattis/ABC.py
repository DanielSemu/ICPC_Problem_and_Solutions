num1,num2,num3=map(int, input().split())
arr=[num1,num2,num3]
arr.sort()
A=arr[0]
B=arr[1]
C=arr[2]
x=input()
for i in range(0,3):
    if x[i]=='A':
        print(A, end=" ")
    elif x[i]=='B':
         print(B, end=" ")
    elif x[i]=='C':
         print(C, end=" ")
print("")
