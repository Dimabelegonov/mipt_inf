def hash(p, m, s):
    a = 0
    for i in range(len(s)):
        a = a + ord(s[i]) * p ** (len(s) - 1 - i)
    return a % m


def insert(hash_table, key, value):
    h = hash(91, 100, key)
    if not hash_table[h % 10]:
        hash_table[h % 10].append([h, key, value])
    else:
        for i in range(len(hash_table[h % 10])):
            if hash_table[h % 10][i][1] == key:
                hash_table[h % 10][i] = [h, key, value]
                break
        else:
            hash_table[h % 10].append([h, key, value])


M = int(input())
hash_table = [[] for _ in range(10)]
for i in range(M):
    s = input().split()
    insert(hash_table, s[0], s[1])

for i in range(10):
    if hash_table[i] != []:
        print(i)
        for a in hash_table[i]:
            print(" ".join(map(str, a)))
