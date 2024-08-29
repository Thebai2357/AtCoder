def ii():  # 数値受け取り 複数対応
    S = input()
    return map(int,S.split()) if " " in S else int(S)
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(map(int,input().split())) for _ in range(N)] if N!= 0 else list(map(int,input().split()))
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

N = ii()
LR = ai(N)
left = 0
right = 0
for i in range(N):
    left+=LR[i][0]
    right+=LR[i][1]
if left>0 or right<0:
    yn(0)
    exit()
else:
    yn(1)
    sum = abs(left)
    for i in range(N):
        if sum>0:
            temp = LR[i][1]-LR[i][0]
            if sum>=temp:
                print(LR[i][1],end = '')
                sum -= temp
            else:
                print(LR[i][0]+sum,end = '')
                sum = 0
        else:
            print(LR[i][0],end = '')
        if i!= N-1:
            print(' ',end = '')
    print()