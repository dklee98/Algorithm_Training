str = input()
out = []
for i in str:
    if 'A' <= i <= 'Z':
        out.append(i)

for i in out:
    print(i, end='')