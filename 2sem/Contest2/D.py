def remove(table, key):
    h = 0
    for i in range(len(key)):
        h = h + ord(key[i]) * 91 ** (len(key) - i - 1)
    h = h % 100

    for i in range(len(table[h % 10])):
        if table[h % 10][i] == []:
            continue

        elif table[h % 10][i][0] == h and table[h % 10][i][1] == key:
            z = table[h % 10][i][2]
            table[h % 10].pop(i)
            return z
    return "KeyError"
