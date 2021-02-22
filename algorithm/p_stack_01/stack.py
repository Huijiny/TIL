stack = []

def is_empty():
    return False if len(stack) else True

def push(item):
    stack.append(item)

def pop():
    if not is_empty():
        return stack.pop()
