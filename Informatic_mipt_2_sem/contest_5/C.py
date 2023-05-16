data = [int(a) for a in input().split(" ")]
data = [(data[a], data[a + 1]) for a in range(0, len(data) - 1, 2)]

x, y = map(int, input().split())

answer = []
for a, b in data:
    # r = ((a - x) ** 2 + (b - y) ** 2) ** 0.5
    vect_x = x - a
    vect_y = y - b
    a += 2 * vect_x
    b += 2 * vect_y
    answer.append(a)
    answer.append(b)

print(*answer)
