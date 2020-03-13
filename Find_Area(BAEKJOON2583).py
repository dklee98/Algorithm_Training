m, n, k = map(int, input().split(' '))
space = [[0] * n for _ in range(m)]
check = [[False] * n for _ in range(m)]

# 사각형 그리기
for i in range(k):
    x1, y1, x2, y2 = map(int, input().split(' '))
    for j in range(y1, y2):
        for k in range(x1, x2):
            space[j][k] = 1

area_cnt = 0


def Bfs(i, j):
    global area_cnt
    q = list()
    q.append((i, j))
    check[i][j] = True
    areas = 1
    while q:
        x, y = q.pop(0)
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if not check[nx][ny] and space[nx][ny] != 1:
                q.append((nx, ny))
                areas += 1
                check[nx][ny] = True
    area_cnt += 1
    return areas


# BFS
area_list = list()

for i in range(m):
    for j in range(n):
        if not check[i][j] and space[i][j] != 1:
            area = Bfs(i, j)
            area_list.append(area)
area_list = sorted(area_list)
print(area_cnt)
for i in range(len(area_list)):
    print(area_list[i], end=' ')
