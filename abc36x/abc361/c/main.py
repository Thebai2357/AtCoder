def ii():  # 数値受け取り 複数対応
    S = input()
    return map(int,S.split()) if " " in S else int(S)
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(map(int,input().split())) for _ in range(N)] if N!= 0 else list(map(int,input().split()))
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")


N,K = ii()
A = ai()
A.sort()
length = N-K
diff = A[-1] - A[0]
for i in range(K+1):
    temp = A[i+length-1] -A[i]
    diff = min(A[i+length-1] -A[i],diff)
print(diff)