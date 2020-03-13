n = input()
set = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
use = [0 for _ in range(10)]

for i in n:
    use[int(i)] += 1
if use.index(max(use)) == 6:
    use[6] -= (use[6] - use[9]) // 2
elif use.index(max(use)) == 9:
    use[9] -= (use[9] - use[6]) // 2

print(max(use))
