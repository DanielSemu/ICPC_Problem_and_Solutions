def func(string):
    string = list(string)
    string.append("")
    out = []
    x = 0
    for i in range(len(string)):
        if i < len(string) - 1:
            if (string[i] in string) is True:
                x += 1
            if string[i] != string[i + 1]:
                if x != 1:
                    out.append(str(x) + string[i])
                    x = 0
                else:
                    out.append(str(x) + string[i])
                    x = 0
    return out

x=input()
output = func(x)
xx=''.join(output)
if(xx[0]==xx[6]):
    print("correct")
else:
    print("fix")


    

  


