x1, y1, x2, y2 = map(int, input().split())
xA, yA = map(int, input().split())
if x1 == x2:
    if xA > x1:
        xB = x1 - abs(x1 - xA)
    else:
        xB = x1 + abs(x1 - xA)
    yB = yA

elif y1 == y2:
    if yA > y1:
        yB = y1 - abs(y1 - yA)
    else:
        yB = y1 + abs(y1 - yA)
    xB = xA

else:
    k1 = (y2 - y1) / (x2 - x1)
    b1 = -(y2 - y1) / (x2 - x1) * x1 + y1
    k2 = -(x2 - x1) / (y2 - y1)
    b2 = yA - k2 * xA

    x0 = (b2 - b1) / (k1 - k2)
    y0 = k1 * x0 + b1

    xvec = x0 - xA
    yvec = y0 - yA

    xB = xvec + x0
    yB = yvec + y0

if int(xB) == xB and int(yB) == yB:
    print(xB, yB, sep=" ")
else:
    print(round(xB, 5), round(yB, 5), sep=" ")
