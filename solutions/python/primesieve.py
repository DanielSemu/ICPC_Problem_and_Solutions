def isprime(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                print("0")
                break
        else:
            print("1")
    else:
        print("0")
def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    count=0
    for p in range(2, n+1):
        if prime[p]:
            count+=1
    print(count)
if __name__ == '__main__':
    n,x=map(int,input().split())
    SieveOfEratosthenes(n)
    for i in range(x):
        y=int(input())
        isprime(y)
    