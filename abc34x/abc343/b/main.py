def i():
    return int(input())
def ii():  # 数値受け取り 複数対応
    return map(int,input().split())
def ai(N = 1):  # 配列受け取り 複数列対応
    return [list(ii()) for _ in range(N)] if N!= 1 else list(ii())
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

N = i()
A = ai(N)

for i in range(N):
    ans_list = []
    for j in range(N):
        if A[i][j] == 1:
            ans_list.append(j+1)
    if ans_list:
        print(*ans_list)

