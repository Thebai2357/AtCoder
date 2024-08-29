def i():
    return int(input())
def ii():  # 数値受け取り 複数対応
    return map(int,input().split())
def ai(N = 1):  # 配列受け取り 複数列対応
    return [list(ii()) for _ in range(N)] if N!= 1 else list(ii())
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

N=i()
A=ai()
M=i()
B=ai()
L=i()
C=ai()
Q=i()
X=ai()

sum_set=set()

for n in range(N):
    for m in range(M):
        for l in range(L):
            sum_set.add(A[n]+B[m]+C[l])
for q in range(Q):
    yn(X[q] in sum_set)
        
