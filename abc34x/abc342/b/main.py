def i():
    return int(input())
def ii():  # 数値受け取り 複数対応
    return map(int,input().split())
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(ii()) for _ in range(N)] if N!= 0 else list(ii())
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

N = i()
P = ai()
Q = i()
AB =ai(Q)
for ab in AB:
    for i in range(N):
        if P[i] == ab[0]:
            print(ab[0])
            break
        elif P[i] == ab[1]:
            print(ab[1])
            break
        else:
            continue
