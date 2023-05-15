x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
N = int(input())

for i in range(N):
    x3, y3 = map(int, input().split())
    l1 = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
    l2 = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
    if 2 * l1 / l2 <= 1:
        print(i + 1)
        break
else:
    print(-1)
