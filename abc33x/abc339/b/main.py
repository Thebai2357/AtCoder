def i():
    return int(input())
def ii():  # 数値受け取り 複数対応
    return map(int,input().split())
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(ii()) for _ in range(N)] if N!= 0 else list(ii())
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

H,W,N=ii()
def pr(k):
    for data in k:
        for i in range(len(data)):
            print(data[i],end = '')
        print('')
def move(now,dir):
    if dir%2 == 0:
        temp = dir-1
        now = [(now[0]+temp)%H,now[1]]
    else:
        temp = dir-2
        now = [now[0],(now[1]-temp)%W]
    return now
    

grid = [['.' for i in range(W)] for j in range(H)]
now = [0,0]    # 縦、横の順
dir = 0 # 0:上 1: 右 2: 下 3: 左 

for tern in range(N):
    if grid[now[0]][now[1]] == '.':
        grid[now[0]][now[1]] = '#'
        dir = (dir+1)%4
    else:
        grid[now[0]][now[1]] = '.'
        dir = (dir-1)%4
    now = move(now,dir)
pr(grid)

