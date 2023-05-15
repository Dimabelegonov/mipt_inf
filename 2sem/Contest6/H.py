a = input().split()
cords = []
ord = []
cnt = 0

while (a[0] != "end"):
    if a[0] == "add":
        cords.append([float(a[2]), float(a[3])])
        k = int(a[1])
        ord.append(-1)
        if ord[k] == -1:
            ord[k] = k
        else:
            tmp = ord[k]
            for i in range(k + 1, len(ord)):
                ord[i], tmp = tmp, ord[i]
            ord[k] = cnt
        cnt += 1
    else:
        area = 0
        for i in range(1, len(ord) - 1):
            area += abs(
                (cords[ord[i]][0] - cords[ord[0]][0]) * (cords[ord[i + 1]][1] - cords[ord[0]][1]) - (
                        cords[ord[i + 1]][0] - cords[ord[0]][0]) * (
                        cords[ord[i]][1] - cords[ord[0]][1])) / 2

        print(round(area, 5))

    a = input().split()
