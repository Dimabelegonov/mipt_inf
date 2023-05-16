a0, b0, c0 = map(int, input().split())
a1, b1, c1 = map(int, input().split())


if a1 * b0 - a0 * b1 != 0:
    y = (a0 * c1 - a1 * c0) / (a1 * b0 - a0 * b1)
    if a0 != 0:
        x = ((b0 * y + c0) / a0) * (-1)
        print(round(x), round(y))
    else:
        print("NO")
else:
    print("NO")

