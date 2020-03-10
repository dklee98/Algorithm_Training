data = list(map(int, input().split(' ')))   #input data


def Merge(arr1, arr2):  # Merge two list to one list
    out_arr = []    # output list
    i = j = 0   # each list's index
    # append data in order
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            out_arr.append(arr1[i])
            i += 1
        else:
            out_arr.append(arr2[j])
            j += 1
    # append remained data (why do not order remained data? arr1 and arr2 are already ordered)
    if i == len(arr1):
        while j < len(arr2):
            out_arr.append(arr2[j])
            j += 1
    else:
        while i < len(arr1):
            out_arr.append(arr1[i])
            i += 1
    return out_arr

# Sperate arr until len(arr) == 1 using recursive function
# Order element by Merge()
def Sort(arr):
    if len(arr) == 1:
        return arr
    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        left1 = Sort(left)
        right1 = Sort(right)
        arr = Merge(left1, right1)
        return arr

# output part
data = Sort(data)
for i in range(len(data)):
    print(data[i])
