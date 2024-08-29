def i():
    return int(input())
def ii():  # 数値受け取り 複数対応
    return map(int,input().split())
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(ii()) for _ in range(N)] if N!= 0 else list(ii())
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

N,M =ii()
A = ai()
B = ai()
A.sort()
B.sort()
b = 0
count = 0
for a in range(N):
    if A[a] >= B[b]:
        count+=A[a]
        b+=1
        if b == M:
            print(count)
            exit()
print(-1)