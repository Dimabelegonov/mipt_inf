"""
Двоичная куча  — такое двоичное подвешенное дерево, для которого выполнены следующие три условия:

1)Значение в любой вершине не больше (если куча для минимума), чем значения её потомков

2)На i-ом слое 2i вершин, кроме последнего. Слои нумеруются с нуля

3)Последний слой заполнен слева направо
"""

"""
Родитель - i
Дети - 2*i+1, 2*i+2

Деть - i
Родитель - (i-1)//2

Высота - log(2)N+1

Прикол кучи - быстро:
1)min/max
2)добавлять
3)удалять
"""

"""
Реализация:
"""


def add_to_heap(heap, elem):
    heap.append(elem)
    shift_up(heap, len(heap) - 1)


def shift_up(heap, i):
    if i == 0:
        return

    parent_i = (i - 1) // 2
    if heap[i] < heap[parent_i]:
        heap[i], heap[parent_i] = heap[parent_i], heap[i]
        shift_up(heap, parent_i)


def pop_from_heap(heap):
    if len(heap) == 0:
        raise ValueError("heap is empty")

    result = heap[0]
    if len(heap) == 1:
        heap.pop()
        return result

    heap[0] = heap.pop()
    shift_down(heap, 0)
    return result


def shift_down(heap, i):
    if 2 * i + 2 < len(heap):
        m = min(heap[i], heap[2 * i + 1], heap[2 * i + 2])
    elif 2 * i + 1 < len(heap):
        m = min(heap[i], heap[2 * i + 1])
    else:
        m = heap[i]

    if m == heap[i]:
        return
    if m == heap[2 * i + 1]:
        heap[i], heap[2 * i + 1] = heap[2 * i + 1], heap[i]
        shift_down(heap, 2 * i + 1)
    elif m == heap[2 * i + 2]:
        heap[i], heap[2 * i + 2] = heap[2 * i + 2], heap[i]
        shift_down(heap, 2 * i + 2)


heap = []
for i in range(5):
    add_to_heap(heap, int(input()))
    # используется shift_up()

print(heap)

for i in range(5):
    print(pop_from_heap(heap))
#   используется shift_down()

"""
Сортировка кучей - O(NlogN)
logN - heapify
N - для каждого элемента
"""
