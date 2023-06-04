try:
    while 1:
        x=input()
        if x =='':
            break
        l=len(x)
        sum=0
        c1=c2=c3=c4=c5=c6=0
        for i in range(l):
            if x[i]=='1':
                c1+=1
                sum+=1
            elif x[i]=='2':
                c2+=1
                sum+=2
            elif x[i]=='3':
                c3+=1
                sum+=3
            elif x[i]=='4':
                c4+=1
                sum+=4
            elif x[i]=='5':
                c5+=1
                sum+=5
            elif x[i]=='6':
                c6+=1
                sum+=6
        rem=31-sum
        if rem<1 and l%2==0:
            print(x, " B") 
        elif rem<1 and l%2!=0:
            print(x," A")
        elif rem>6 and l%2==0:
            print(x, " A")
        elif rem>6 and l%2!=0:
            print(x," B")
        elif rem == 1:
            print(c1)
            if l%2==0 and c1<4:
                print(x," A")
            elif l%2!=0 and c1<4:
                print(x," B")
            elif l%2==0 and c1>=4:
                print(x," B")
            elif l%2!=0 and c1>=4:
                print(x," A")
        else:
            while 1:
                r1=str(rem)
                if x.count(r1)<4:
                    if l%2==0:
                        print(x," A")
                        break
                    else:
                        print(x ," B")
                        break
                else:
                    rem-=1
except:
    pass


# print(c1)
# print('Mary had a little laamb'.count('a'))
# if rem<1 and l%2==0:
#     print(x, " B") 
# elif rem<1 and l%2!=0:
#     print(x," A")
# elif rem>6 and l%2==0:
#     print(x, " A")
# elif rem>6 and l%2!=0:
#     print(x," B")
# elif rem==1:
#     if l%2==0 and c1<4:
#         print(x," A")
#     elif l%2!=0 and c1<4:
#         print(x," B")
#     elif l%2==0 and c1>=4:
#         print(x," B")
# elif rem==2:
#     if l%2==0 and (c1<4 or c2<4):
#         print(x," A")
#     elif l%2!=0 and (c1<4 or c2<4):
#         print(x," B")
#     elif l%2==0 and c1>=4:
#         print(x," B")







# # if rem<1 and l%2==0:
# #     print(x, " A") 
# # elif rem<1 and l%2!=0:
# #     print(x," B")
# # elif rem>=1:
# #     if l%2==0:
# #         if rem==1 and c1<4:
# #             print()
# #         elif rem==2 and c2<4:
# #             print()
# #         elif rem==3 and c3<4:
# #             print()
# #         elif rem==4 and c4<4:
# #             print()
# #         elif rem==5 and c5<4:
# #             print()
# #         elif rem==6 and c6<4:
# #             print()

# #     else:
# #         if rem==1 and c1<4:
# #             print()
# #         elif rem==2 and c2<4:
# #             print()
# #         elif rem==3 and c3<4:
# #             print()
# #         elif rem==4 and c4<4:
# #             print()
# #         elif rem==5 and c5<4:
# #             print()
# #         elif rem==6 and c6<4:
# #             print()
