def ii():  # 数値受け取り 複数対応
    S = input()
    return map(int,S.split())
def ai(N = 1):  # 配列受け取り 複数列対応
    return [list(ii()) for _ in range(N)] if N!= 1 else list(ii())
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

S = list(input())
if S[0] != "<":
    yn(0)
    exit()
elif S[-1] != ">":
    yn(0)
    exit()
else:
    for i in range(1,len(S)-1):
        if S[i] != "=":
            yn(0)
            exit()
yn(1)
