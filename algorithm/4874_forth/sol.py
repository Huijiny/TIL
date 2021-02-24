import sys
sys.stdin = open("sample_input (1).txt")

T = int(input())
for tc in range(1, T+1):
    result = 0
    tmp = input().split()
    stack = []
    opt = 0
    for i in range(len(tmp)-1):
        if tmp[i].isdigit():
            stack.append(tmp[i])
        if tmp[i] == '.':
            if len(stack) != 1:
                result = 'error'
                break
            result = stack.pop()
            break
        elif tmp[i] == '+' or tmp[i] == '-' or tmp[i] == '*' or tmp[i] == '/':
            try:
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                if tmp[i] == '+':
                    stack.append(n1+n2)
                elif tmp[i] == '-':
                    stack.append(n1-n2)
                elif tmp[i] == '/':
                    stack.append(n1//n2)
                elif tmp[i] == '*':
                    stack.append(n1*n2)
            except:
                opt = 1
                break
    if opt == 1 or len(stack) != 1:
        result = 'error'
    else:
        result = stack.pop()
    print("#{} {}".format(tc, result))