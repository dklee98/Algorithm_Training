import queue

r, c = map(int, input().split(' '))
data = [list(input()) for _ in range(r)]
check = [[False] * c for _ in range(r)]
sheep = wolf = 0

def Bfs(i, j):
    global sheep, wolf
    q = queue.Queue()
    q.put((i, j))
    check[i][j] = True
    o, v = 0, 0
    while not q.empty():
        x, y = q.get()
        if data[x][y] == 'o':
            o += 1
        if data[x][y] == 'v':
            v += 1
        for dx, dy in (-1,0), (1,0), (0,-1), (0,1):
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if not check[nx][ny] and data[nx][ny] != '#':
                q.put((nx, ny))
                check[nx][ny] = True
    if o > v:
        sheep += o
    else:
        wolf += v


for i in range(r):
    for j in range(c):
        if not check[i][j] and data[i][j] != '#':
            Bfs(i, j)
print(sheep, wolf)