data = list(map(int, input().split(' ')))


def Heapify(arr):
    if len(arr) == 1:
        return arr
    for leaf in range(len(arr) - 1, 0, -1):
        root = (leaf - 1) // 2
        if arr[root] < arr[leaf]:
            arr[root], arr[leaf] = arr[leaf], arr[root]
    return arr


def Heap_Sort(arr):
    arr = Heapify(arr)
    end = len(arr) - 1
    if end != 0:
        arr[0], arr[end] = arr[end], arr[0]
        end -= 1
        arr[:end + 1] = Heap_Sort(arr[:end + 1])
    return arr


data = Heap_Sort(data)
for i in range(len(data)):
    print(data[i])