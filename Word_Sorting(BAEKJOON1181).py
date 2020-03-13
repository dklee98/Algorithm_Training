total_word = int(input())
word_arr = []
for k in range(total_word):
    word_arr.append(input())


def Sort(arr):
    arr = list(set(arr))
    arr = Heap_Sort(arr, True)
    # print(arr)
    arr = Sort_by_alpa(arr)
    # print(arr)
    return arr


def Heapify(arr):
    leaf = len(arr) - 1
    for i in range(leaf, 0, -1):
        root = (i - 1) // 2
        if len(arr[root]) < len(arr[i]):
            arr[root], arr[i] = arr[i], arr[root]
    # print(arr)
    return arr


def Heapify_Alpa(arr):
    leaf = len(arr) - 1
    for i in range(leaf, 0, -1):
        root = (i - 1) // 2
        if ascii(arr[root]) < ascii(arr[i]):
            arr[root], arr[i] = arr[i], arr[root]
    # print(arr)
    return arr


def Heap_Sort(arr, flag):
    if len(arr) == 1:
        return arr
    if flag:
        arr = Heapify(arr)
    else:
        arr = Heapify_Alpa(arr)
    end = len(arr) - 1
    if end != 0:
        arr[0], arr[end] = arr[end], arr[0]
        arr[:end] = Heap_Sort(arr[:end], flag)
    return arr


def Sort_by_alpa(arr):
    cnt = [0]
    output_arr = []
    for i in range(len(arr) - 1):
        if len(arr[i]) != len(arr[i + 1]):
            cnt.append(i + 1)
    cnt.append(len(arr))
    for i in range(len(cnt) - 1):
        same_arr = arr[cnt[i]:cnt[i + 1]]
        output_arr += Heap_Sort(same_arr, False)
    return output_arr


word_arr = Sort(word_arr)
for i in range(len(word_arr)):
    print(word_arr[i])
