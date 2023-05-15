def ph(s):
    root = 37
    hash = [0]
    p = 1
    for c in s:
        hash.append(((hash[-1] * root) % mod + ord(c)) % mod)
        p = (p * root) % mod
    return (hash, p)


mod = 10 ** 9 + 7

sample = input()
text = input()
s_hash, p = ph(sample)
s_hash = s_hash[-1]
t_hash, _ = ph(text)
x = []

for left_lim in range(len(text) - len(sample) + 1):
    right_lim = left_lim + len(sample)
    if s_hash == (t_hash[right_lim] - (t_hash[left_lim] * p) % mod) % mod:
        x.append(str(left_lim))
if not x:
    print(-1)
else:
    print(' '.join(x))

"""Изначальный код"""

# def hash(s):
#     p, m = 13, 256
#     a = 0
#     for i in range(len(s)):
#         a = a + ord(s[i]) * p ** (len(s) - i - 1)
#     return a % m
#
#
# def check(a1, a2):
#     h1 = hash(a1)
#     p, m = 13, 256
#     hashSum = hash(a2[:len(a1)])
#     res = []
#
#     for i in range(len(a2) - len(a1) + 1):
#         if h1 == hashSum and a1 == a2[i:i + len(a1)]:
#             res.append(i)
#         if i < len(a2) - len(a1):
#             hashSum = ((hashSum - (ord(a2[i]) * p ** (len(a1) - 1))) * p + ord(a2[i + len(a1)])) % m
#             if hashSum < 0:
#                 hashSum += m
#
#     if not res:
#         print(-1)
#     else:
#         print(' '.join(map(str, res)))
#
#
# a1, a2 = input(), input()
# check(a1, a2)
