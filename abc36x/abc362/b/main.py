def ii():  # 数値受け取り 複数対応
    S = input()
    return map(int,S.split()) if " " in S else int(S)
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(map(int,input().split())) for _ in range(N)] if N!= 0 else list(map(int,input().split()))
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

xy = ai(3)

f = pow(xy[0][0]-xy[1][0],2)+pow(xy[0][1]-xy[1][1],2)
s = pow(xy[2][0]-xy[1][0],2)+pow(xy[2][1]-xy[1][1],2)
t = pow(xy[0][0]-xy[2][0],2)+pow(xy[0][1]-xy[2][1],2)
hen = [f,s,t]
hen.sort()
if hen[1]+hen[0] == hen[2]:
    yn(1)
else:
    yn(0)