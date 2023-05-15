N = int(input())
a = []
cnt = 0

for i in range(N):
    a.append(list(map(float, input().split())))

x, y = map(float, input().split())

for i in range(len(a)):
    if i == len(a) - 1:
        x1, x2, y1, y2 = a[i][0], a[0][0], a[i][1], a[0][1]
    else:
        x1, x2, y1, y2 = a[i][0], a[i + 1][0], a[i][1], a[i + 1][1]

    if y2 <= y <= y1 or y1 <= y <= y2:
        if x1 == x2 and x1 <= x:
            cnt += 1
        elif y1 == y2:
            if x2 <= x <= x1 or x1 <= x <= x2:
                cnt = 1
                break
        else:
            z = (x2 - x1) * (y - y1) / (y2 - y1) + x1
            if z < x:
                cnt += 1
            elif z == x:
                cnt = 1
                break

if cnt % 2 == 1:
    print("YES")
else:
    print("NO")
