def ii():  # 数値受け取り 複数対応
    S = input()
    return map(int,S.split()) if " " in S else int(S)
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(map(int,input().split())) for _ in range(N)] if N!= 0 else list(map(int,input().split()))
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

S=input()
T=input()
s0 = ord(S[0])
s1 = ord(S[1])
sd = abs(s0-s1)

t0 = ord(T[0])
t1 = ord(T[1])
td = abs(t0-t1)
yn(sd==td or sd+td==5)