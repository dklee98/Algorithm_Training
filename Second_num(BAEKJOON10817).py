input_data = input().split(' ')
a = int(input_data[0])
b = int(input_data[1])
c = int(input_data[2])
num = [a,b,c]
num.remove(max(a,b,c))
num.remove(min(a,b,c))
print(num.pop())
