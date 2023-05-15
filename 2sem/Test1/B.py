a = list(map(int, input().split()))
b = list(map(int, input().split()))
arr = []
for i in range(len(a)):
    for j in range(len(b)):
        arr.append(b[j])
        if b[j] == a[i]:
            break

print(" ".join(map(str, arr)))
