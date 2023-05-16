stack = []

t = input()
while t != "=":
    if t.isdigit() or t[1::].isdigit():
        stack.append(int(t))
    else:
        a = stack.pop()
        b = stack.pop()
        if t == "-":
            stack.append(b - a)
        elif t == "+":
            stack.append(a + b)
        else:
            stack.append(a * b)
    t = input()

print(stack[-1])
