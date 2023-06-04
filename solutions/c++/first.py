a,b,c=map(int,input().split())
a=a%1000000007
b=b%1000000007
c=c%1000000007
ansa=((a%c) + (b%c))%c
ansb=((a%c) - (b%c))%c
ansc=((a%c) * (b%c))%c
print(ansa,ansb,ansc)