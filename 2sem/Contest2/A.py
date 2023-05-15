def hash(p, m, s):
    a = 0
    for i in range(len(s)):
        a = a + ord(s[i]) * p ** (len(s) - i - 1)
    return a % m


p, m = map(int, input().split())
s = input()
print(hash(p, m, s))
