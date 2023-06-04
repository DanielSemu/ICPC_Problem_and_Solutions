num = int(input())
num2 = num+1
num = num+1
def palin(num):
    pal = 0
    while num != 0:
        mod = num % 10
        pal = (pal*10)+mod
        num = (num//10)
    return pal


while True:
    if palin(num) == num2:
        print(num)
        break
    else:
        num = num+1
        num2 = num2+1