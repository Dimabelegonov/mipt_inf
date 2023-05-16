s = list(map(int, input()))

for i in range(len(s)):
    if i < len(s) - 1:
        print(str(s[i]) + "*10^" + str(len(s) - i - 1) + " + ", end="")
    else:
        print(str(s[i]) + "*10^" + str(len(s) - i - 1), end="")
