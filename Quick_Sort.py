def Quick_Sort(arr, start, end):
    if start >= end:    # this means arr has one element
        return
    key = start # set pivot
    i = high_index = start  #   i, j is index
    j = low_index = end     #   high_index finds element that is bigger than key, low index finds element that is smaller then key
    while low_index > high_index:   # before swap, low_index has to be bigger than high_index
        while arr[i] <= arr[key] and i < end:   # check element that is bigger than key in order from left
            i += 1
        high_index = i                          # and save that index
        while arr[j] > arr[key] and j > start:  # check element that is smaller then key in order from right
            j -= 1
        low_index = j                           # and save that index
        if low_index <= high_index:             #  this situation means numbers except key already divided into small side and large side
            arr[key], arr[low_index] = arr[low_index], arr[key] # then, key has to go to right place
            Quick_Sort(arr, start, low_index - 1)               # Do Quick sort on small one side
            Quick_Sort(arr, low_index + 1, end)                 # Do Quick sort on large one side
        else:                                   # this situation means two numbers(low, high index) have to change their place
            arr[low_index], arr[high_index] = arr[high_index], arr[low_index]       # so change their place to divided two side(small one, large one)


num = list(map(int, input().split(' ')))    # input data
Quick_Sort(num, 0, len(num) - 1)    # sort function
for k in range(len(num)):   # print part
    print(num[k])
