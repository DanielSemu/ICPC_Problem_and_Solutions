 #     s = sum(map(int, str(number)))
def harsh(n):
    sum = 0
    while (n != 0):
        sum = sum + (n % 10)
        n = n//10
        return sum
    return n % sum == 0


n = int(input())
while True:
    if harsh(n):
        print(n)
        break
    else:
        n += 1
# x=123
# s = sum(map(int, str(x)))
# print(s)