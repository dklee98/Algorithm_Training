T = input()
nums = []
for i in range(int(T)):
    nums.append(int(input()))

def Factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * Factorial(n - 1)

for number in nums:
    cnt = 0
    for i in range((number // 3)+1):
        for j in range((number // 2)+1):
            for k in range((number // 1)+1):
                if number == 3 * i + 2 * j + 1 * k:
                    cnt += Factorial(i+j+k) // (Factorial(i) * Factorial(j) * Factorial(k))

    print(cnt)