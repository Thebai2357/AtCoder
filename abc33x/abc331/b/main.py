def ii():  # 数値受け取り 複数対応
    S = input()
    return map(int,S.split()) if " " in S else int(S)
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(map(int,input().split())) for _ in range(N)] if N!= 0 else list(map(int,input().split()))
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

N,S,M,L = ii()

dp = [pow(10,6)]*(N+1)
dp[0] = 0
for i in range(1,N+1):
    dp[i] = min(dp[max(i-6,0)]+S,dp[max(i-8,0)]+M,dp[max(i-12,0)]+L)
print(dp[N])