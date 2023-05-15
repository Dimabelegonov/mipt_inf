def search(table, key):
    h = 0
    for i in range(len(key)):
        h = h + ord(key[i]) * 91 ** (len(key) - i - 1)
    h = h % 100

    for x in table[h % 10]:
        if x == []:
            continue

        elif x[0] == h and x[1] == key:
            return x[2]
    return "KeyError"
