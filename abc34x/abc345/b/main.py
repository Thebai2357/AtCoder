def i():
    return int(input())
def ii():  # 数値受け取り 複数対応
    return map(int,input().split())
def ai(N = 1):  # 配列受け取り 複数列対応
    return [list(ii()) for _ in range(N)] if N!= 1 else list(ii())
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

X = i()
if X>0:
    if X%10 == 0:
        print(X//10)
    else:
        print(X//10+1)
else:
    if X%10 == 0:
        print(X//10)
    else:
        print(X//10+1)