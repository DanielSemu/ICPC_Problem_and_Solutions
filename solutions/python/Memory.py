di={
    'int': 4,
    'double':8,
    'bool': 1,
    'char': 1,
    'float':4,
}
t=0
for _ in range(int(input())):
    a,b= map(str, input().split())
    b=int(b)
    t+=di[a]*b

print(t)