def quarter(dot):
    if dot[0] > 0 and dot[1] > 0:
        return 1
    if dot[0] < 0 and dot[1] > 0:
        return 2
    if dot[0] < 0 and dot[1] < 0:
        return 3
    if dot[0] > 0 and dot[1] < 0:
        return 4
    if dot[0] == 0 and dot[1] > 0:
        return "up0"
    if dot[0] == 0 and dot[1] < 0:
        return "down0"
    if dot[0] > 0 and dot[1] == 0:
        return "right0"
    if dot[0] < 0 and dot[1] == 0:
        return "left0"


N = int(input())
cords = []
k = []
for i in range(N):
    x, y = map(int, input().split())
    cords.append([x, y])
    if x == 0:
        k.append("vertical")
    else:
        k.append(y / x)

max = 1
for i in range(len(k) - 1):
    cnt = 1
    for j in range(i + 1, len(k)):
        if k[i] == k[j] and quarter(cords[i]) == quarter(cords[j]):
            cnt += 1
    if cnt > max:
        max = cnt

print(max)
