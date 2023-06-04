x =int(input())
height = []
count = 1
for i in range (x):
    y = [list(k) for k in input().split()]
    height.append(y)

height = int(height)

for i in range(x):
    if(height[i]- height[i+1]>0):
        count +=1
    
print(count)
