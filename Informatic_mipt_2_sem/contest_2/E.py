def search(line: str, s: str) -> list:
    hash_s = hash(s)
    answer = []
    for i in range(len(line)):
        p_line = line[i:i+len(s)]
        # print(p_line, hash(p_line))
        if hash_s == hash(p_line):
            answer.append(str(i))

    return answer


if __name__ == "__main__":
    a = input()
    s = input()
    answer = search(s, a)
    if len(answer) != 0:
        print(" ".join(answer))
    else:
        print("")
