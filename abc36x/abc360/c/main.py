def ii():  # 数値受け取り 複数対応
    S = input()
    return map(int,S.split()) if " " in S else int(S)
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(map(int,input().split())) for _ in range(N)] if N!= 0 else list(map(int,input().split()))
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

N = ii()
A = ai()
W = ai()
adict = {}
sum = 0
for i in range(N):
    if A[i] not in adict:
        adict[A[i]] = W[i]
    else:
        if adict[A[i]]<=W[i]:
            sum += adict[A[i]]
            adict[A[i]]=W[i]
        else:
            sum+=W[i]
print(sum)