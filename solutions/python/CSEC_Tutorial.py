from math import ceil
x,y,z,m=map(int, (input().split()))
n=ceil(x/y)
min=n*m
max=ceil(((z*x)+x)/y) * m
print(min ,max)