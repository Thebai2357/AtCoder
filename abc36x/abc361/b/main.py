def ii():  # 数値受け取り 複数対応
    S = input()
    return map(int,S.split()) if " " in S else int(S)
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(map(int,input().split())) for _ in range(N)] if N!= 0 else list(map(int,input().split()))
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

a,b,c,d,e,f = ai()
g,h,i,j,k,l = ai()
same = []

def myfunc(a,d,g,j):
    if a>g:
        if j<=a:
            yn(0)
            exit()
    else:
        if d<=g:
            yn(0)
            exit()

myfunc(a,d,g,j)
myfunc(b,e,h,k)
myfunc(c,f,i,l)
yn(1)