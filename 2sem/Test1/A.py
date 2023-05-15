a = input()
stack = []
check = 1

for i in range(len(a)):
    if a[i] in "({[":
        stack.append(a[i])
    else:
        if len(stack) > 0:
            el = stack.pop(-1)
            if a[i] == ")" and el == "(":
                continue
            elif a[i] == "]" and el == "[":
                continue
            elif a[i] == "}" and el == "{":
                continue
            else:
                print("NO")
                check = 0
                break

if check == 1:
    if len(stack) == 0:
        print("YES")
    if len(stack) != 0:
        print("NO")
