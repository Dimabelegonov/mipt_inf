def add_to_heap(h, element):
    h.append(element)
    shift_up(h, len(h) - 1)


def shift_up(h, i):
    if i == 0:
        return
    parent_i = (i - 1) // 2
    if h[i] < h[parent_i]:
        h[i], h[parent_i] = h[parent_i], h[i]
        shift_up(h, parent_i)


N = int(input())
a = list(map(int, input().split()))
h = []
for i in range(N):
    add_to_heap(h, a[i])

print(' '.join(map(str, h)))
