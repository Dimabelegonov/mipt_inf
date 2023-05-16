data = {}
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    if x == 0:
        if y > 0:
            k = "vert+"
        else:
            k = "vert-"
    else:
        k = y / x
        if k == 0:
            if x > 0:
                k = "right"
            else:
                k = "left"
        else:
            if x > 0 and y > 0:
                k = str(k) + "1"
            elif x > 0 and y < 0:
                k = str(k) + "2"
            elif x < 0 and y > 0:
                k = str(k) + "3"
            elif x < 0 and y < 0:
                k = str(k) + "4"

    if k in data.keys():
        data[k] += 1
    else:
        data[k] = 1

ans = 0
for key in data.keys():
    ans = max(ans, data[key])

print(ans)
