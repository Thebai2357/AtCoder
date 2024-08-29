def ii():  # 数値受け取り 複数対応
    S = input()
    return map(int,S.split()) if " " in S else int(S)
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(map(int,input().split())) for _ in range(N)] if N!= 0 else list(map(int,input().split()))
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

H,W = ii()
S = ai()
C = [list(input()) for i in range(H)]
X = list(input())
hnow,wnow= S[0]-1,S[1]-1
for dir in X:
    if dir == 'L':
        if wnow != 0:
            if C[hnow][wnow-1] == '.':
                wnow-=1
    elif dir =='R':
        if wnow != W-1:
            if C[hnow][wnow+1] == '.':
                wnow+=1
    elif dir == 'U':
        if hnow!= 0:
            if C[hnow-1][wnow] == '.':
                hnow -=1
    else:
        if hnow != H -1:
            if C[hnow+1][wnow] == '.':
                hnow+=1
print(hnow+1,wnow+1)