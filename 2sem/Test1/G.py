a = list(map(int, input().split()))
stack = []

for i in range(len(a) - 1):
    if a[i] > 0:
        stack.append(a[i])
    elif len(stack) > 0:
        if abs(a[i]) < stack[-1]:
            stack[-1] += a[i]
        else:
            stack.pop(-1)

print(len(stack), stack[-1] if len(stack) != 0 else -1, sep=" ")
