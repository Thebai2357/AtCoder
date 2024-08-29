def ii():  # 数値受け取り 複数対応
    S = input()
    return map(int,S.split()) if " " in S else int(S)
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(map(int,input().split())) for _ in range(N)] if N!= 0 else list(map(int,input().split()))
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

N = ii()
S = list(input())

def win(a):
    if a == "R":
        return "P"
    elif a == "P":
        return "S"
    else:
        return "R"


bef_win,bef_even = "A","A"
cnt_win,cnt_even = 0,0
for i in range(N):
    next = win(S[i])
    temp = 0
    if next !=bef_win:
        temp = cnt_win+1
    if next != bef_even:
        if cnt_even+1>temp:
            temp = cnt_even+1
    
    temp2 = 0
    if S[i] != bef_win:
        temp2 = cnt_win
    if S[i] != bef_even:
        if cnt_even>temp2:
            temp2 = cnt_even
    
    bef_even = S[i]
    bef_win = next
    cnt_win,cnt_even = temp,temp2
    # print(temp,temp2)
    # print(i,cnt_win,cnt_even)

print(max(cnt_even,cnt_win))

