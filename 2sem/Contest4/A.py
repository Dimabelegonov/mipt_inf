a = input().split()
stack = []
cnt = 0
for i in range(len(a)):
    stack.append(a[i])
    if len(stack) >= 2:

        if stack[-2][0] == stack[-1][0] and abs(int(stack[-2][1]) - int(stack[-1][1])) <= 2:
            stack.pop(-1)
            stack.pop(-1)
            cnt += 2

            if len(stack) >= 2:

                if stack[0][0] == stack[-1][0]:
                    stack.pop(0)
                    stack.pop(-1)
                    cnt += 2
    else:
        continue

print(cnt)
