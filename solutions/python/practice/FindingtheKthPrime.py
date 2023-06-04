lst=[]
def seive():
    n=90000001
    prime=[True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    for i in range(2,n+1):
        if prime[i]:
            lst.append(i)
x=int(input())
seive()
for i in range(x):
    num=int(input())
    print(lst[num-1])
    
