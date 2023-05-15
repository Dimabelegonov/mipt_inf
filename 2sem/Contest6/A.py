x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())

cent_distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
if (x1 - x2) ** 2 + (y1 - y2) ** 2 < r2 ** 2:
    if (cent_distance + r1) >= r2:
        print("YES")
    else:
        print("NO")
elif (x2 - x1) ** 2 + (y2 - y1) ** 2 < r1 ** 2:
    if cent_distance + r2 >= r1:
        print("YES")
    else:
        print("NO")
elif cent_distance <= r1 + r2:
    print("YES")

else:
    print("NO")
