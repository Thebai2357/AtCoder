def ii():  # 数値受け取り 複数対応
    S = input()
    return map(int,S.split()) if " " in S else int(S)
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(map(int,input().split())) for _ in range(N)] if N!= 0 else list(map(int,input().split()))
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

Y = ii()

if Y%400 == 0:
    print("366")
elif Y%100 == 0:
    print("365")
elif Y%4 == 0:
    print("366")
else:
    print("365")