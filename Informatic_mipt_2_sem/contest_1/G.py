def get_ans(k, m):
    if m == 1:
        return k

    return 2 * k + get_ans(k + 1, m - 1)

k = int(input())
m = int(input())
print(get_ans(k, m))
