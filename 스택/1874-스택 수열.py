text = input()

while text != '.':
    stack = []
    for char in text:
        if char == '(' or char == ')':
            stack.append(char)
            if stack[-1] == '(' and stack[-2] == ')':
                stack.pop()
                stack.pop()
        if char == '[' or char == ']':
            stack.append(char)
            if stack[-1] == '[' and stack[-2] == ']':
                stack.pop()
                stack.pop()
    if len(stack) == 0:
        print("yes")
    else:
        print("no")
    text = input()