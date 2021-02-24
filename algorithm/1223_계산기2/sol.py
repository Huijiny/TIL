import sys
sys.stdin = open("input (4).txt")

T = 10
for tc in range(1, T+1):
    # 후위 표기법으로 변환한다.
    N = int(input())
    expr = input()
    stack_str = []
    stack_num = []
    for i in expr:
        if i == '+' or i == '*':
            if len(stack_str) == 0:
                stack_str.append(i)
            else:
                tmp = stack_str.pop()
                if i == '+':
                    stack_num.append(tmp)
                    stack_str.append(i)

                elif i == '*':
                    if tmp == '+':
                        stack_str.append(tmp)
                        stack_str.append(i)
                    else:
                        stack_num.append(tmp)
                        stack_str.append(i)
        else:
            stack_num.append(i)

    for i in range(len(stack_str)):
        stack_num.append(stack_str.pop())
    cal_stack = []

    for i in stack_num:
        if i == '*' or i == '+':
            n1 = int(cal_stack.pop())
            n2 = int(cal_stack.pop())
            if i == '*':
                cal_stack.append(n1 * n2)
            else:
                cal_stack.append(n1 + n2)
        else:
            cal_stack.append(i)

    print("#{} {}".format(tc, cal_stack[0]))