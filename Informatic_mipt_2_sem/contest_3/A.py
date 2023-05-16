data = list(map(str, input().split()))
stack = []
ans = []

for card in data:
    if len(stack) > 0:
        if stack[-1][0] == card[0] and abs(int(stack[-1][1]) - int(card[1])) <= 2:
            ans.append(card)
            ans.append(stack.pop())

            while len(stack) > 1 and stack[-1][0] == stack[0][0]:
                ans.append(stack.pop(0))
                ans.append(stack.pop())
        else:
            stack.append(card)
    else:
        stack.append(card)


print(len(ans))
