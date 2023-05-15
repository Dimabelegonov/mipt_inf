a = list(map(int, input().split()))
x, y = map(int, input().split())

for i in range(0, len(a), 2):
    xvec = x - a[i]
    yvec = y - a[i + 1]
    xnew = xvec + x
    ynew = yvec + y
    print(xnew, ynew, sep=" ", end=" ")
