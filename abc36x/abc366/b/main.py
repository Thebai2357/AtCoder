def ii():  # 数値受け取り 複数対応
    S = input()
    return map(int,S.split()) if " " in S else int(S)
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(map(int,input().split())) for _ in range(N)] if N!= 0 else list(map(int,input().split()))
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")
N = ii()
S = [list(input()) for i in range(N)]
lenmax = 0
for i in range(N):
    if len(S[i])>lenmax:
        lenmax = len(S[i])
for i in range(lenmax):
    output = ""
    for j in range(N):
        if len(S[N-j-1])>=i+1:
            output = output+S[N-j-1][i]
        else:
            output+="*"
    while output[-1] == "*":
        output = output[:-1]
    print(output)