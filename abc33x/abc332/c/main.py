def ii():  # 数値受け取り 複数対応
    S = input()
    return map(int,S.split()) if " " in S else int(S)
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(map(int,input().split())) for _ in range(N)] if N!= 0 else list(map(int,input().split()))
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

N,M = ii()
S = list(input())

white = M
buy = 0
need = 0

for schedule in S:
    schedule = int(schedule)
    if schedule == 0:
        buy = max(buy,need)
        white = M
        need = 0
    elif schedule == 1:
        if white != 0:
            white -= 1
        else:
            need+=1
    else:
        need+=1
buy = max(buy,need)
print(buy)

