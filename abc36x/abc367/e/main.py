def ii():  # 数値受け取り 複数対応
    S = input()
    return map(int,S.split()) if " " in S else int(S)
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(map(int,input().split())) for _ in range(N)] if N!= 0 else list(map(int,input().split()))
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")


N,K = ii()
X = ai()
A = ai()
A_origin = A.copy()

def next(A,X):
    B =[]
    for i in range(N):
        B.append(A[X[i]-1])
    return B

for i in range(K):
    A = next(A,X)
for i in range(K):
    A = next(A,X)
    if A == A_origin:
        break
K = K%i
for i in range(K):
    A = next(A,X)
print(A)