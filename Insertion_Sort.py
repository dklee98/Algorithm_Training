num = list(map(int, input().split(' ')))
for i in range(len(num)-1):
    index = i
    while index >= 0 and num[index] > num[index+1]:
        num[index], num[index+1] = num[index+1], num[index]
        index -= 1
for i in range(len(num)):
    print(num[i])