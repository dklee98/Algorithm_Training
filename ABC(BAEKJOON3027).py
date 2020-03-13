nums = list(map(int,input().split(' ')))
abc = input()

sorted_nums = sorted(nums)
arr = []
for i in range(3):
    if abc[i] == 'A':
        arr.append(sorted_nums[0])
    elif abc[i] == 'B':
        arr.append(sorted_nums[1])
    elif abc[i] == 'C':
        arr.append(sorted_nums[2])

for i in range(3):
    print(arr[i], end=' ')