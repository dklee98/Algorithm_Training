data1, data2 = input().split(' ')
str1 = list(data1)
str1.reverse()
num1 = int("".join(str1))

str2 = list(data2)
str2.reverse()
num2 = int("".join(str2))

if num1 > num2 :
    print(num1)
else:
    print(num2)


