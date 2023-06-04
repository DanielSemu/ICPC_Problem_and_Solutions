
import re
vowels='e'
x=input()
str_list = re.findall(f'[{vowels}]', x, re.I)
w=len(str_list)
print("h",end="")
for i in range(w*2):
    print("e",end="")   
print("y")