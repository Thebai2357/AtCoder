def ii():  # 数値受け取り 複数対応
    S = input()
    return map(int,S.split()) if " " in S else int(S)
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(map(int,input().split())) for _ in range(N)] if N!= 0 else list(map(int,input().split()))
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

N = ii()+1

A = [ai(N-1) for i in range(N-1)]
Q = ii()
Asum = [[[0]*N for i in range(N)] for j in range(N)]

for x in range(1,N):
    table = [[0]*N for _ in range(N)]
    for y in range(1,N):
        for z in range(1,N):
            temp = Asum[x-1][y][z]
            table[y][z] = table[y][z-1] +table[y-1][z] - table[y-1][z-1]+A[x-1][y-1][z-1]
            Asum[x][y][z] = temp+table[y][z]
for i in range(Q):
    lx,rx,ly,ry,lz,rz = ii()
    ans = Asum[rx][ry][rz]
    ans = ans - Asum[rx][ly-1][rz] - Asum[lx-1][ry][rz]-Asum[rx][ry][lz-1]
    ans = ans + Asum[lx-1][ly-1][rz]+Asum[lx-1][ry][lz-1]+Asum[rx][ly-1][lz-1]
    ans = ans - Asum[lx-1][ly-1][lz-1]
    print(ans)
