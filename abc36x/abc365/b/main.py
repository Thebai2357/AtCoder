def ii():  # 数値受け取り 複数対応
    S = input()
    return map(int,S.split()) if " " in S else int(S)
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(map(int,input().split())) for _ in range(N)] if N!= 0 else list(map(int,input().split()))
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")
N = ii()
A = ai()
co = A.copy()
co.sort()
co.pop(-1)
print(A.index(co.pop(-1))+1)