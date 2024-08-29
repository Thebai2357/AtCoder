def i():
    return int(input())
def ii():  # 数値受け取り 複数対応
    return map(int,input().split())
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(ii()) for _ in range(N)] if N!= 0 else list(ii())
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

Q =i()
query = ai(Q)
A = []
for que in query:
    if que[0] == 1:
        A.append(que[1])
    else:
        print(A[-que[1]])