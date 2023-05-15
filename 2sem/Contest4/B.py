a = input().split()
stack = []
for i in range(len(a)):
    if len(stack) == 0 and a[i] == "#" or len(stack) < 2 and a[i] == "%":
        print(float(0))
        break

    if a[i] == "#":
        c = 0
        for j in range(len(stack)):
            c += stack.pop()
        stack.append(c)

    elif a[i] == "%":
        stack.append(stack.pop(-1) * stack.pop(-1) / 100)

    else:
        stack.append(a[i])
else:
    if len(a) == 0:
        print(float(0))
    else:
        print(float(stack[-1]))
