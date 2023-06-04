from math import floor
s=input()
sume=0
for i in s:
    sume+=ord(i)
total=sume+100-(sume%100)

ans=(sume/total)*100
ans=100-floor(ans)
print(str(ans)+"%")