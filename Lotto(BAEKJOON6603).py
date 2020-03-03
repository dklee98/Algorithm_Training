arr_set = []
index = 0
while True:
    input_data = input()
    if input_data == '0':
        #print("끝")
        break
    else:
        k = int(input_data.split(' ')[0])
        s = input_data.split(' ')[1:]
        if k < 7 or k > 12 or len(s) != k:
            print("제대로 입력하시오")
            continue
        else:
            index += 1
            arr_set.append(s)


def nC6(arr):
    result = []
    for a in range(len(arr) - 6 + 1):
        result.append(arr[a])
        for b in range(a + 1, len(arr) - 6 + 2):
            result.append(arr[b])
            for c in range(b + 1, len(arr) - 6 + 3):
                result.append(arr[c])
                for d in range(c + 1, len(arr) - 6 + 4):
                    result.append(arr[d])
                    for e in range(d + 1, len(arr) - 6 + 5):
                        result.append(arr[e])
                        for f in range(e + 1, len(arr) - 6 + 6):
                            result.append(arr[f])
                            for i in range(6):
                                print(int(result[i]), end=' ')
                            print("")
                            result.pop()
                        result.pop()
                    result.pop()
                result.pop()
            result.pop()
        result.pop()


for i in range(index):
    nC6(arr_set[i])
    if i != index-1:
        print("")
