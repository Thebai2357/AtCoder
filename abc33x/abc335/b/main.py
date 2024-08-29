def i():
    return int(input())
def ii():  # 数値受け取り 複数対応
    return map(int,input().split())
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(ii()) for _ in range(N)] if N!= 0 else list(ii())
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

N =i()
for x in range(N+1):
    for y in range(N+1):
        for z in range(N+1):
            if x+y+z<=N:
                print(x,y,z)