lst=[]
def prime(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    for p in range(2, n+1):
        if prime[p]:
           lst.append(p)
 
while 1:
    x=int(input())
    if x== -1:
        break
    prime(x)
    min=x
    for i in range(len(lst)):
        n=lst[i]
        y=x-n
        if y in lst:
            if (abs(n-y)<min):
                min=abs(n-y)
                num1=lst[i]
    n=x-num1
    if(n<num1):
        print(n," ",num1)
    else:
        print(num1," ",n)
