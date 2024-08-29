def ii():  # 数値受け取り 複数対応
    S = input()
    return map(int,S.split())
def ai(N = 1):
    return [list(ii()) for _ in range(N)] if N!= 1 else list(ii())
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

W,B=ii()

wloop = 9
bloop = 6
