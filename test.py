from sys import stdin

def isBal(string):
    stk = []
    for e in string:
        if e == '(' or e == '[':
            stk.append(e)
        elif e == ')':
            if len(stk) == 0 or stk.pop() == '[':
                return 'no'
        elif e == ']':
            if len(stk) == 0 or stk.pop() == '(':
                return 'no'
    if len(stk): return 'no'
    return 'yes'

while True:
    string = str(stdin.readline().rstrip())
    if string == '.':
        break
    else:
        print(isBal(string))

                
    
