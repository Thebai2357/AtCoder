def i():
    return int(input().split())
def ii():  # 数値受け取り 複数対応
    S = input()
    return map(int,S.split())
def ai(N = 1):
    return [list(ii()) for _ in range(N)] if N!= 1 else list(ii())
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

N,K = ii()
A = ai()

sum = 0
sum_list = set()
for i in range(len(A)):
    if A[i] not in sum_list and A[i]<=K:
        sum += A[i]
        sum_list.add(A[i])
print(K*(K+1)//2-sum)