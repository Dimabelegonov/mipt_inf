def check_diag(arr):
    for i in range(len(arr)):
        if arr[i][i] != 0:
            return False
    return True


def check_sym(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != arr[j][i]:
                return False
    return True


def check_matrix(arr):
    if check_diag(arr) and check_sym(arr):
        return "YES"
    else:
        return "NO"


n = int(input())
arr = []
for i in range(n):
    a = list(map(int, input().split()))
    arr.append(a)
print(check_matrix(arr))
