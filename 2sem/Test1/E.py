def func(a):
    stack = []
    for i in range(len(a)):
        if a[i] == "+":
            if len(stack) >= 2:
                x = stack.pop()
                y = stack.pop()
                stack.append(int(x) + int(y))
            else:
                return "incorrect"
        elif a[i] == "*":
            if len(stack) >= 2:
                x = stack.pop()
                y = stack.pop()
                stack.append(int(x) * int(y))
            else:
                return "incorrect"
        elif a[i] == "-":
            if len(stack) >= 2:
                x = stack.pop()
                y = stack.pop()
                stack.append(int(y) - int(x))
            else:
                return "incorrect"
        elif a[i] == "/":
            if len(stack) >= 2:
                x = stack.pop()
                y = stack.pop()
                stack.append(int(y) // int(x))
            else:
                return "incorrect"
        else:
            stack.append(a[i])
    if len(stack) != 2:
        return "incorrect"
    else:
        return stack[0]


a = input().split()
var = {}

for i in range(len(a)):
    if a[i] in "*+-=/" or a[i].isdigit() == True:
        continue
    else:
        if a[i][0].isdigit() == True:
            print("incorrect")
            break
        else:
            var[a[i]] = 0
else:
    for i in range(len(var)):
        b = input().split()
        if b[0] in var:
            var[b[0]] = int(b[1])
        else:
            print("incorrect")
            break
    else:
        for i in range(len(a)):
            if a[i] in var:
                a[i] = var[a[i]]
            elif a[i].isdigit() == True:
                a[i] = int(a[i])
        print(func(a))
