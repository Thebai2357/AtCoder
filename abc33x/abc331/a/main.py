def ii():  # 数値受け取り 複数対応
    S = input()
    return map(int,S.split()) if " " in S else int(S)
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(map(int,input().split())) for _ in range(N)] if N!= 0 else list(map(int,input().split()))
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")
M,D =ii()
y,m,d = ii()
upm = 0
d = d+1
if d>D:
    upm = 1
    d = 1
upy = 0
m=m+upm
if m>M:
    upy = 1
    m = 1
y += upy
print(y,m,d)