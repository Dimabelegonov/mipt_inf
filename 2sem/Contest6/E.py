a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

if a1 * b2 == a2 * b1:
    print("NO")
else:
    y = (b1 * c2 - b2 * c1) / (a1 * b2 - a2 * b1)
    x = -(a2 * y + c2) / b2
    print(round(y), round(x), sep=" ")
