def main():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j and matrix[i][i] != 0:
                return False
            if matrix[i][j] != matrix[j][i]:
                return False

    return True


if main():
    print("YES")
else:
    print("NO")
