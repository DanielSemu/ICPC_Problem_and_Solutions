from posixpath import split


while 1:
    x=int(input())
    if x==-1:
        break
    lst = [int(i) for i in input().split()]
    lst.sort()
    for i in range(len(lst)):
        print(lst[i],end=" ")
    print()