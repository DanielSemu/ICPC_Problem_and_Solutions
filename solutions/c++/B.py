x=input()

for i in range(len(x)-4):
    if (x[i]=='R'and x[i+1]=="B" and x[i+2]=="L") or  (x[i]=='R'and x[i+1]=="L" and x[i+2]=="B") or  (x[i]=='B'and x[i+1]=="R" and x[i+2]=="L") or  (x[i]=='B'and x[i+1]=="L" and x[i+2]=="R") or  (x[i]=='L'and x[i+1]=="R" and x[i+2]=="B") or  (x[i]=='L'and x[i+1]=="B" and x[i+2]=="R"):
        print('C')
        i=i+3
    elif x[i]=='R':
        print('S')
    elif x[i]=='B':
        print('K')
    elif x[i]=='L':
        print('H')
