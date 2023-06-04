# x=int(input())
# st=[str(i) for i in input().split()]
# st1=[]
# for i in range(len(st)):
#     if st[i] =='T':
#         st1.append(True)
#     elif st[i] =='F':
#         st1.append(False)
# op=[str(i) for i in input().split()]
# for i in range(len(op)):
#     if op[i]=='*':
#         v=st1[0] and st1[1]
#         st1.remove(st1[0])
#         st1.remove(st1[1])
#         st1.append(v)
#     elif op[i]=='+':
#         v=st1[0] or st1[1]
#         st1.remove(st1[0])
#         if len(st1)>1:
#             st1.remove(st1[1])
#         st1.append(v)
#     elif op[i]=='-':
#         v= not st1[0]
#         st1.remove(st1[0])
#         st1.append(v)
# if(st1[0]== True):
#     print("T")
# elif st1[0] ==False:
#     print("F")
########################

def evaluate(var_vals, exp):
    var_stack, op_stack = ([],[])
    ops = {
        '*': lambda: var_stack.pop() and var_stack.pop(),
        '+': lambda: var_stack.pop() or var_stack.pop(),
        '-': lambda: not var_stack.pop()
    }

    for c in exp:
        if c in ops:
            op_stack.insert(0, c)
        else:
            var_stack.insert(0, var_vals[ord(c) - 65])

    while op_stack:
        var_stack.append(ops[op_stack.pop()]())

    return var_stack.pop()

def main():
    input() # dump
    var_vals=list(map(lambda z: True if z=='T' else False, input().split()))
    exp = input().split()
    print('T' if evaluate(var_vals, exp) else 'F')

if __name__ == "__main__":
    main()

    
