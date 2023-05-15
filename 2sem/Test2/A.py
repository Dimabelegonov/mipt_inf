N = int(input())
dict = {}
for _ in range(N):
    a = input().lower()
    if a not in dict:
        dict[a] = 1
    else:
        dict[a] += 1
maxk = -1
for el in dict:
    if dict[el] > maxk:
        maxk = dict[el]
        maxel = el

print(maxel, maxk)
