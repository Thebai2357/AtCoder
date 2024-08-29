def ii():  # 数値受け取り 複数対応
    S = input()
    return map(int,S.split()) if " " in S else int(S)
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(map(int,input().split())) for _ in range(N)] if N!= 0 else list(map(int,input().split()))
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

Q = ii()
dec = {}
count = 0
for i in range(Q):
    q = ai()
    if len(q) == 1:
        print(count)
    elif q[0] == 1:
        x = q[1]
        if x not in dec:
            count+=1
            dec[x] = 1
        else:
            dec[x] +=1
    elif q[0] == 2:
        x = q[1]
        if dec[x] == 1:
            count-=1
            dec.pop(x)
        else:
            dec[x]-=1



