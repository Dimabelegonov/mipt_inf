data = list(map(int, input().split()))
n = len(data)
print(*data)


for _ in range(n):
    for i in range(n - 1):
        if data[i] > data[i + 1]:
            data[i], data[i + 1] = data[i + 1], data[i]
            print(*data)
