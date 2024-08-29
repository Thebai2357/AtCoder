def i():
    return int(input())
def ii():  # 数値受け取り 複数対応
    return map(int,input().split())
def ai(N = 1):  # 配列受け取り 複数列対応
    return [list(ii()) for _ in range(N)] if N!= 1 else list(ii())
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

N,M=ii()
H = ai()
temp = M
for i in range(N):
    if H[i]<=temp:
        temp -=H[i]
    else:
        print(i)
        exit()
print(N)