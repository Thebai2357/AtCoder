def i():
    return int(input())
def ii():  # 数値受け取り 複数対応
    return map(int,input().split())
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(ii()) for _ in range(N)] if N!= 0 else list(ii())
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

N = i()-1
ans = ''
if N == 0:
    print(0)
    exit()
while(True):
    if N==0:
        print(ans)
        exit()
    temp = N%5
    ans = str(temp*2)+ans
    N = N//5
