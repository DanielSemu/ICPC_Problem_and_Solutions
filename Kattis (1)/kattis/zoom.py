# n,k=map(int, input().split())
# lst=list(map(int, input().split()))
# for i in range(k-1,n+1,k):
#     print(lst[i], end=" ")
# @Dăņį§ď'őŋě, [7/25/22 3:28 PM]
_n, k = map(int, input().split())
ns = list(map(int, input().split()))
print(*ns[k-1::k])