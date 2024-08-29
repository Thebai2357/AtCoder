def i():
    return int(input())
def ii():  # 数値受け取り 複数対応
    return map(int,input().split())
def ai(N = 1):  # 配列受け取り 複数列対応
    return [list(ii()) for _ in range(N)] if N!= 1 else list(ii())
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

S = list(input())
normal = S[0]
if S[1] != normal:
    if S[2] != S[1]:
        print(2)
    else:
        print(1)
else:
    for i in range(2,len(S)):
        if S[i] != normal:
            print(i+1)
            break