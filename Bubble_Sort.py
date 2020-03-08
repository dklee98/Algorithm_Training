num = list(map(int, input().split(' ')))
for k in range(len(num) - 1):
    for i in range(len(num) - k - 1):
        if num[i] > num[i+1]:
            num[i], num[i+1] = num[i+1], num[i]
for i in range(len(num)):
    print(num[i])