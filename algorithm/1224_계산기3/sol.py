import sys
sys.stdin = open("input (4).txt")
T = 10

for tc in range(1, T+1):
    n = input()
    result = 0
    expression = input()
    stack_num = []
    stack_str = []
    for i in expression:
        if i.isdigit():
            stack_num.append(i)
        else:
            if i == '(':
                stack_str.append(i)
            if i == ')':
                popped = ''
                while popped != '(':
                    popped = stack_str.pop()
                    if popped != '(':
                        stack_num.append(popped)
            if i == '+' or i == '*':
                if len(stack_str) == 0:
                    stack_str.append(i)
                else:
                    tmp = stack_str.pop()
                    if i == '+':
                        if tmp == '(':
                            stack_str.append(tmp)
                            stack_str.append(i)
                        else:
                            stack_num.append(tmp)
                            stack_str.append(i)

                    elif i == '*':
                        if tmp == '+' or tmp == '(':
                            stack_str.append(tmp)
                            stack_str.append(i)
                        else:
                            stack_num.append(tmp)
                            stack_str.append(i)

    for i in range(len(stack_str)):
        stack_num.append(stack_str.pop())

    cal_stack = []
    for i in stack_num:
        if i.isdigit():
            cal_stack.append(i)
        else:
            n1 = int(cal_stack.pop())
            n2 = int(cal_stack.pop())
            if i == '+':
                cal_stack.append(n1+n2)
            elif i == '*':
                cal_stack.append(n1*n2)

    print("#{} {}".format(tc, cal_stack[0]))