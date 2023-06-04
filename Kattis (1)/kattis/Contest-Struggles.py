n,k= map(int, input().split())
d,s= map(int, input().split())
tot=n*k
rem=n-k
curr=k*s
if(tot - curr > 100 * rem):
      print("impossible")
else:
    print((tot - curr) / rem)

    
    