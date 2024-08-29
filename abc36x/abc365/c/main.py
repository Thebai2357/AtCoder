def ii():  # 数値受け取り 複数対応
    S = input()
    return map(int,S.split()) if " " in S else int(S)
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(map(int,input().split())) for _ in range(N)] if N!= 0 else list(map(int,input().split()))
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

N,M = ii()
A = ai()

all  = sum(A)

if all<=M:
    print("infinite")
    exit()

hmax = max(A)
hmin = 0
while hmax-hmin > 1:
    mid = (hmin+hmax)//2
    all = 0
    for i in range(N):
        all +=min(A[i],mid)
    if all>M:
        hmax = mid
    else:
        hmin = mid
all = 0
for i in range(N):
    all +=min(A[i],hmax)
if all<=M:
    print(hmax)
else:
    print(hmin)