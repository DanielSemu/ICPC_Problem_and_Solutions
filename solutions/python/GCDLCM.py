
def gcd(a, b):
    if a == 0 :
        return b
     
    return gcd(b%a, a)
x=0
while True:
    num1=int(input())
    if num1==-1:
        break
    num2=int(input())
    gg=gcd(num1, num2)
    ll=int((num1*num2)/gg)
    print(gg," ",ll)
 
