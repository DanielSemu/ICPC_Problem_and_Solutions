import math
case = 1
while True:

    num = input().split()
    if int(num[0]) == 0 and int(num[1]) == 0:
        break
    else:
        R = int(num[0])
        N = int(num[1])
        lef = R-N
        if N*26 < lef:
            print(f"Case { case}: impossible")
            case += 1
        else:
            print(f"Case { case}: {math.ceil(lef/N)}")
            case += 1