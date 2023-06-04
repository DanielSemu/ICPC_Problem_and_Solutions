x= int(input())
while(x>0):
    if(x%2==1):
        x= (x*3)+1
    else:
        x = x/2;
        print(x);
    if(x == 1):
        print(x)
        break;