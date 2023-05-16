def check(x1, x2):
    s1 = ((x1 - a1) ** 2 + (x2 - a2) ** 2) ** 0.5
    s2 = ((x1 - b1) ** 2 + (x2 - b2) ** 2) ** 0.5
    if s1 < s2 // 2:
        return True
    return False


a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
n = int(input())
data = []
for _ in range(n):
    data.append(map(int, input().split()))


def main():
    for i, (a1, a2) in enumerate(data):
        if check(a1, a2):
            return i + 1
    return -1


print(main())
