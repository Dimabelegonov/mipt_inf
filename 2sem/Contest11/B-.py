def check(N, K):
    win = [-1] * (N + 1)
    win[0] = 0
    for i in range(1, N + 1):
        if i < K:
            for j in range(0, i):
                if win[j] == 0:
                    win[i] = 1
                    break
                else:
                    continue
            else:
                win[i] = 0

        else:
            for j in range(i - K, i):
                if win[j] == 0:
                    win[i] = 1
                    break
                else:
                    continue
            else:
                win[i] = 0
    return ''.join(map(str, win)), len(win)


N, K = map(int, input().split())
list = list(map(int, input().split()))
bin_array = []
maxlen = -1
for i in range(N):
    bin, length = check(list[i], K)
    bin_array.append(bin)
    if length > maxlen:
        maxlen = length

for i in range(len(bin_array)):
    if len(bin_array[i]) < maxlen:
        while len(bin_array[i]) != maxlen:
            bin_array[i] += "x"
a = bin_array[0]
for i in range(1, len(bin_array)):
    new_a = str()
    for j in range(len(bin_array[i])):
        if bin_array[i][j] == "x" or a[j] == "x":
            new_a += "x"
        elif bin_array[i][j] == a[j]:
            new_a += "0"
        else:
            new_a += "1"
    a = new_a
if a[-1] == "0":
    print("NO")
else:
    print("YES")
