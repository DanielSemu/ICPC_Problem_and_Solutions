n = 5  # how many numbers to accept
lst = [int(num) for num in input().split(" ", n-1)]

#lst = list(map(int, input().split()))
if(lst[1]+lst[3])<=lst[4]:
    print(lst[0]+lst[2])
elif(lst[1]>lst[4] or lst[3]>lst[4]):
    print()
else:
    print(max(lst[0],lst[2]))


# #     function knapsackLight(value1, weight1, value2, weight2, maxW) {
# #   var val;
# #   if (lst[2] > lst[0]) {
# #     lst[0],lst[2]=lst[2],lst[0]
# #     lst[1],lst[3]=lst[3],lst[1]
# #   }
# #   val = 0;
# #   if (weight1 <= maxW) {
# #     val += lst[0];
# #     maxW -= weight1
# #   }
# #   if (weight2 <= maxW)
# #     val += value2;

# #   return val;
# from math import floor


# m1,m12,m11,s= map(int, input().split())
# re =0
# if s>=m1:
#     s-=m1
#     re+=1
# if(re>0):
#     while(re<=10 and s-m12>=0):
#         re+=1
#         s-=m12
#     while(re>10):
#         re+= floor(s/m11)
#         # s-=m11
# print(re)