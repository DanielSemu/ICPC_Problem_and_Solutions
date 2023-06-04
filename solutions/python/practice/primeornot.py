from cmath import sqrt
def isprime(num):
    if num==1:
        return False
    for i in range(2, sqrt(int(num))):
        if num%i==0:
            return False
    return True
x=int(input())
if isprime(x):
    print("Yes")
else:
    print("No")