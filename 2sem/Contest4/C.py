a = input()
stack = []
while a != "=":
    if a == '+':
        stack.append(int(stack.pop(-1)) + int(stack.pop(-1)))
    elif a == "-":
        stack.append(- int(stack.pop(-1)) + int(stack.pop(-1)))
    elif a == "*":
        stack.append(int(stack.pop(-1)) * int(stack.pop(-1)))
    else:
        stack.append(a)
    a = input()

print(stack[-1])
