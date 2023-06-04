x,y=map(int, input().split())
matrix=[]
for i in range(x):        
    a =[]
    str=input()
    for j in range(y):     
         a.append(str[j])
    matrix.append(a)
for i in range(x-1):
    for j in range(y):
        a=i
        while 1:
            if matrix[a][j] == "a" and matrix[a+1][j]=="#":
                break
            temp=matrix[a][j]
            matrix[a][j]=matrix[a+1][j]
            matrix[a+1][j]=temp
            a+=1
            if a==x-1:
                break

            
for i in range(x):
    for j in range(y):
        print(matrix[i][j],end="")
    print()