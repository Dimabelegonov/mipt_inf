def func(a):
    print(" ".join(map(str, a)))
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                print(" ".join(map(str, a)))
            else:
                continue

a = list(map(int, input().split()))

func(a)
