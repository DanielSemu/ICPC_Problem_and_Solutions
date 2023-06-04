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
while True:
    x=input()
    if x=='""':
        break
    output = func(x)
    print(''.join(output))
    

  


