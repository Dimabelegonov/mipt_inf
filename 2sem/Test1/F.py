N = int(input())
stack = []

for i in range(N):
    a = input().split()
    if len(a) == 2:
        move, num = a[0], a[1]
        if move == "+":
            stack.append(num)
        elif move == "*":
            if len(stack) % 2 == 0:
                pos = len(stack) // 2
            else:
                pos = len(stack) // 2 + 1
            stack.append("new")

            t = stack[pos]
            for j in range(pos + 1, len(stack)):
                t, stack[j] = stack[j], t
            stack[pos] = num

    elif len(a) == 1 and a[0] == "-":
        t = stack.pop(0)
        print(t)
