class Heap():
    def __init__(self):
        self.n = -1
        self.data = []

    def new_element(self, x):
        self.n += 1
        self.data.append(x)
        self.update(self.n)

    def update(self, ind):
        up_ind = (ind - 1) // 2
        if up_ind > -1 and self.data[up_ind] > self.data[ind]:
            self.data[up_ind], self.data[ind] = self.data[ind], self.data[up_ind]
            self.update(up_ind)

    def __str__(self) -> str:
        return " ".join(map(str, self.data))


n = int(input())
data = list(map(int, input().split()))
heap = Heap()
for x in data:
    heap.new_element(x)
    # print(heap)

print(heap)
