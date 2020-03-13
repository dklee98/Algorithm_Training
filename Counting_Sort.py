print("Please enter range : ", end='')
num_range = list(map(int, input().split(' ')))
print("Please enter numbers in the range : ", end='')
data = list(map(int, input().split(' ')))
if num_range[0] > num_range[1]:
    print("ERROR : Enter a valid range")
    exit()
for i in range(len(data)):
    if data[i] < num_range[0] or data[i] > num_range[1]:
        print("ERROR : Enter numbers in the range")
        exit()


count = [0 for i in range(num_range[0], num_range[1] + 1)]
for i in range(len(data)):
    for j in range(num_range[0], num_range[1] + 1):
        if data[i] == j:
            count[j - num_range[0]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(num_range[0] + i, end=' ')