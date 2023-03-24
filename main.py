def RPN_to_INF(RPN,convert):
    stack = []
    string = RPN.split(' ')
    for i in string:
        try:
            char = int(i)
            stack.append(char)
        except:
            v1 = stack.pop()
            v2 = stack.pop()
            if convert == True:
                temp = eval(f'({v2} {i} {v1})')
            else:
                temp = f'({v2} {i} {v1})'
            stack.append(temp)
    return(stack[-1])

print(RPN_to_INF('77 55 + 7 7 7 * * *',False))

def INF_to_RNP(INF):
    return(eval(INF))
