import sys
sys.stdin = open("sample_input (1).txt")

T = int(input())

for tc in range(1, T+1):
    result = 1
    stack = []
    code = input()
    for i in code:
        if i == '(' or i =='{' or i == '[':
            stack.append(i)
        elif i == ')' or i == '}' or i == ']':
            if len(stack) == 0:
                result = 0
                break
            poped = stack.pop()
            if i == ')':
                if poped != '(':
                    result = 0
                    break
            if i == '}':
                if poped != '{':
                    result = 0
                    break
            if i == ']':
                if poped != '[':
                    result = 0
                    break
    if len(stack) != 0:
        result = 0
    print("#{} {}".format(tc, result))