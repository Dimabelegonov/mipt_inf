class Heap():
    def __init__(self, data=None):
        self.n = 0
        self.data = []
        if data:
            for x in data[::-1]:
                self.new_element(x)

    def new_element(self, x):
        self.n += 1
        self.data.append(x)
        self.update(self.n - 1)

    def update(self, ind):
        up_ind = (ind - 1) // 2
        if up_ind > -1 and self.data[up_ind] < self.data[ind]:
            self.data[up_ind], self.data[ind] = self.data[ind], self.data[up_ind]
            self.update(up_ind)

    def get_max(self):
        m = self.data[0]
        if self.n > 1:
            self.data[0] = self.data.pop()
            self.n -= 1
            self.heapify(0)
        return m

    def heapify(self, ind):
        left_child = ind * 2 + 1
        right_child = ind * 2 + 2
        parent = ind
        if left_child < self.n and self.data[left_child] > self.data[parent]:
            self.data[left_child], self.data[parent] = self.data[parent], self.data[left_child]
            self.heapify(left_child)

        if right_child < self.n and self.data[right_child] > self.data[parent]:
            self.data[right_child], self.data[parent] = self.data[parent], self.data[right_child]
            self.heapify(right_child)


    def __str__(self) -> str:
        return " ".join(map(str, self.data))



def heapsort(A:list):
    heap = Heap(data=A)
    for j in range(len(A)):
        for i in range(heap.n):
            A[i] = heap.data[i]
        print(*A)
        A[len(A) - 1 - j] = heap.get_max()


# heapsort(list(map(int, input().split())))

