def listSorter(array: ListToSort) -> ListToSort:
    build_max_heap(array)
    heap_size: int = array.Length()
    for i in range(array.Length() - 1, 0, -1):
        array.Swap(i, 0)
        heap_size -= 1
        max_heapify(array, 0, heap_size)
    return array


def build_max_heap(array: ListToSort):
    heap_size = array.Length()
    for i in range((heap_size // 2) - 1, -1, -1):
        max_heapify(array, i, heap_size)


def max_heapify(array: ListToSort, i: int, heap_size: int):
    if left(i) < heap_size and array.Larger(left(i), i):
        c = left(i)
    else:
        c = i
    if right(i) < heap_size and array.Larger(right(i), c):
        c = right(i)
    if c != i:
        array.Swap(i, c)
        max_heapify(array, c, heap_size)


def left(i: int) -> int:
    return (2 * i) + 1


def right(i: int) -> int:
    return 2 * (i + 1)