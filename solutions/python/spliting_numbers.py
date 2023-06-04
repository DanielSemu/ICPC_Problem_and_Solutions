# while 1:
#   n = int(input())
#   if n == 0:
#     break
#   a = 0
#   b = 0
#   t = True 
#   i = 0
#   while n != 0:
#     bit = n & 1
#     n = n >> 1
#     if bit == 1:
#       if t:
#         a ^= (1 << i)
#       else:
#         b ^= (1 << i)
#       t = not t 
#     i += 1 
#   print ("{} {}".format(a, b))
def check(i,j,n):
    s=0
    k=0
    if i+j==n:
        print('cond checked.. return true for i+j == n')
        return True
    while s<n:
        print('in while loop.....')
        if k%2==0:
            s+=1
        else:
            s+=j
        k+=1
    if s==n:
        print('returned true...')
        return True
    else:
        print('returned false...')

        return False

n = int(input())
print(f'{n}:')
for i in range(2,(n//2)+2):
    print('here..')
    for j in range(i-2,i+1):
        print('second loop...')
        if check(i,j,n)==True:
            print('condition checked..')
            print(f'{i},{j}')