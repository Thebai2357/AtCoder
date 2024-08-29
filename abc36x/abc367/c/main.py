def ii():  # 数値受け取り 複数対応
    S = input()
    return map(int,S.split()) if " " in S else int(S)
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(map(int,input().split())) for _ in range(N)] if N!= 0 else list(map(int,input().split()))
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")
def printif(S,K):
    sum_array = sum(S)
    if sum_array%K == 0:
        print(*S)




N,K = ii()
R = ai()
start = [1]*N
while True:
    printif(start,K)
    start[-1] += 1
    for i in range(N):
        if start[N-1-i]>R[N-1-i]:
            start[N-1-i] = 1
            if N-i-2<0:
                exit()
            start[N-1-i-1]+=1
