def hashing(s: str, a: int, b: int) -> int:
    ahash = 0
    for i in range(len(s)):
        ahash += (ord(s[i]) * (a ** (len(s) - i - 1))) % b

    return ahash % b



if __name__ == "__main__":
    a, b = map(int, input().split())
    s = input()
    print(hashing(s, a, b))

