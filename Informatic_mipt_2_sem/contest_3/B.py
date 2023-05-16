def main():
    data = list(map(str, input().split()))
    queue = []
    while len(data) > 0:
        char = data.pop(0)
        if char.isdigit() or char[1::].isdigit():
            queue.append(float(char))
        else:
            if len(queue) > 0:
                if char == "#":
                    a = sum(queue)
                    queue = [a]
                else:
                    if len(queue) > 1:
                        a = queue.pop()
                        b = queue.pop()
                        queue.append(a * b / 100)
                    else:
                        return 0.0
            else:
                return 0.0
    return queue[-1]


print(main())
