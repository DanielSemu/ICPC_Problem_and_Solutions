# x=input()
# if len(x)==1 and x=='a':
#     print('a')
# elif x[len(x)-1]=='a':
#     print('a')
# for i in range(len(x)-1):
#     if x[i]=='a':
#         z=x[i:len(x)+1]
#         print(z)
#         break

print((lambda w: w[w.find('a'):])(input()))