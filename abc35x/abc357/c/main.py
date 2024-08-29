def i():
    return int(input())
def ii():  # 数値受け取り 複数対応
    return map(int,input().split())
def ai(N = 1):  # 配列受け取り 複数列対応
    return [list(ii()) for _ in range(N)] if N!= 1 else list(ii())
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

N=i()
def carpet(n):  # １辺が3^nのカーペット 白を１
    side = pow(3,n)
    mini_side = pow(3,n-1)
    bg_carpet = [[0 for i in range(side)] for i in range(side)]
    if n!=0:
        sm_carpet = carpet(n-1)
    else:
        return [[0]]

    for yoko in range(side):
        for tate in range(side):
            if yoko // mini_side == 1 and tate // mini_side == 1:
                bg_carpet[tate][yoko] = 1
            else:
                bg_carpet[tate][yoko] = sm_carpet[tate%mini_side][yoko%mini_side]
    return bg_carpet
side = pow(3,N)
result = carpet(N)
for tate in range(side):
    for yoko in range(side):
        if result[tate][yoko] ==0:
            print('#',end = '')
        else:
            print('.',end = '')
    print('')
