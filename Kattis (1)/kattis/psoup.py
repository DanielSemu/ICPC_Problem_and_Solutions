n = int(input())
count = 0
for _ in range(n):
    k = int(input())
    name = input()
    m = set(input() for _ in range(k))
    if 'pea soup' in m and 'pancakes' in m:
        count +=1 
        print(name)
        break
if count<1:
    print('Anywhere is fine I guess')
    