def hashing(s: str, a=91, b=100) -> int:
    ahash = 0
    for i in range(len(s)):
        ahash += (ord(s[i]) * (a ** (len(s) - i - 1))) % b

    return ahash % b


def insert(table: list, key: str, value:str):
    ahash = str(hashing(key))
    ind = int(ahash) % mod
    if len(table[ind]) == 0:
        table[ind].append([ahash, key, value])
    else:
        flag = True
        for i, el in enumerate(table[ind]):
            if el[1] == key:
                table[ind][i][2] = value
                flag = False
        if flag:
            table[ind].append([ahash, key, value])


def search(table: list, key: str) -> str:
    ahash = str(hashing(key))
    for i, el in enumerate(table[int(ahash) % mod]):
        if el[1] == key:
            return el[2]

    return "KeyError"


def remove(table, key):
    ahash = str(hashing(key))
    ind = int(ahash) % mod
    for i, el in enumerate(table[ind]):
        if el[1] == key:
            data = table[ind].pop(i)
            return data[2]

    return "KeyError"


# if __name__ == "__main__":
#     mod = 10
#     n = int(input())
#     data = []
#     hash_table = [[] for _ in range(10)]
#     for _ in range(n):
#         key, value = map(str, input().split())
#         insert(hash_table, key, value)

#     for i, el in enumerate(hash_table):
#         if len(el) != 0:
#             print(i)
#             for elem in el:
#                 print(*elem)


if __name__ == "__main__":
    mod = 10
    # example_table = [
    #     [], [],
    #     [
    #         [32, 'ONLY', 'pal;cw'],
    #         [62, 'INDUSTRY', 'lfow'],
    #         [72, 'LETRASET', 'awdwad'],
    #         [32, 'BEEN', 'lkawdk'],
    #     ],
    #     [], [], [], [], [], [], [],
    # ]
    # v1 = remove(example_table, 'BEEN')      # v1 == 'lkawdk'
    # v2 = remove(example_table, 'PRODUCT')   # v2 == 'KeyError'
    # print(v1)
    # print(v2)
    # print(example_table)