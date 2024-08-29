def ii():  # 数値受け取り 複数対応
    S = input()
    return map(int,S.split()) if " " in S else int(S)
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(map(int,input().split())) for _ in range(N)] if N!= 0 else list(map(int,input().split()))
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

N = ii()
H = ai()

count = 0
turn = 0
for enemy in range(N):
    mod = H[enemy]%5
    for _ in range(3):
        if mod<=0:
            break
        if turn%3==0:
            mod-=1
        elif turn%3==1:
            mod-=1
        else:
            mod-=3
        turn +=1
        count+=1
    count+=(H[enemy]//5)*3
print(count)
    