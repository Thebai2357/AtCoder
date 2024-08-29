def ii():  # 数値受け取り 複数対応
    S = input()
    return map(int,S.split()) if " " in S else int(S)
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(map(int,input().split())) for _ in range(N)] if N!= 0 else list(map(int,input().split()))
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

N,Q = ii()
R = ai()
R.sort()
query = []
for i in range(Q):
    query.append([ii(),i])
query.sort()

dier_sum = 0
que_num = 0
ans_list=[]
for sled in range(N):
    dier_sum+=R[sled]
    while True:
        if que_num==Q:
            break
        que = query[que_num]
        if que[0]<dier_sum:
            ans_list.append([sled,que[1]])
            que_num+=1
        else:
            break
for i in range(que_num,Q):
    que = query[i]
    ans_list.append([N,que[1]])
ans_list.sort(key=lambda x: x[1])
for i in range(Q):
    print(ans_list[i][0])