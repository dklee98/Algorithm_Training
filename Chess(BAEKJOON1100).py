space = []
for i in range(8):
    space.append(input())
white = [[False] * 8 for _ in range(8)]


for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            white[i][j] = True
            cnt = 0

for i in range(8):
    for j in range(8):
        if white[i][j] and space[i][j] == 'F':
            cnt += 1

print(cnt)