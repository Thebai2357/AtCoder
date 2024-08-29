def ii():  # 数値受け取り 複数対応
    S = input()
    return map(int,S.split()) if " " in S else int(S)
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(map(int,input().split())) for _ in range(N)] if N!= 0 else list(map(int,input().split()))
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

sx,sy =ii()
tx,ty =ii()
if sx>tx:
    sx,sy,tx,ty = tx,ty,sx,sy
dif=abs(ty-sy)
sx = sx+((sx+sy)%2!=0)
tx = tx-(tx+ty)%2
tmax = sx+dif
if tx>tmax:
    dif+=(tx-tmax+1)//2
print(dif)