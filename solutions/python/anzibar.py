
t = int(input())
count=[]
while t:
    x = list(map(int, input().split()))
    if len(x) == 1:
        print(0)
        continue
    count=[]
    for i in range(1, len(x)):
        if x[i] > 2 * x[i - 1]:
                count.append(x[i]-(2*x[i-1]))

    print(sum(count))
    t-=1