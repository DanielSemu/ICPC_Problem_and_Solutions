x=int(input())
for i in range(x):
    y=input()
    numbers = [int(num) for num in input().split()]
    cost=0
    str=input()
    l=len(str)
    ls=[]
    s3=''
    s1=str[0:numbers[0]]
    s2=str[numbers[0]:l+1]
    print(s1)
    ls += [s1]
    ls += [s2]
    for k in range(len(str)):
            if str[k] in s1 and str[k] in s2:
                continue
            else:
                if str[k] in s3:
                    continue
                else:
                    s3=s3+str[k]
                    cost+=1 
    for j in range(1,len(numbers)):
        print(ls[0])
        while 1:
            e=0
            ll=len(ls[e])
            if numbers[e]<ll:
                break
            else:
                e+=1
                ll+=len(ls[e])

        s1=ls[e][0:numbers[j]]
        s2=ls[e][numbers[j]:l+1]
        l1=len(s1)
        l2=len(s2)
        s3=''
        for k in range(len(str)):
            if str[k] in s1 and str[k] in s2:
                continue
            else:
                if str[k] in s3:
                    continue
                else:
                    s3=s3+str[k]
                    cost+=1   
    print(cost)



       
        
        


