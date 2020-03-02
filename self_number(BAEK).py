all_num = set(range(1, 10001))
dn_num = set()
for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    dn_num.add(i)
a = all_num - dn_num
for i in sorted(a):
    print(i)