def ii():  # 数値受け取り 複数対応
    S = input()
    return map(int,S.split()) if " " in S else int(S)
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(map(int,input().split())) for _ in range(N)] if N!= 0 else list(map(int,input().split()))
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

N,M = ii()
A = ai()
sum_list=[0]
for i in range(N):
    sum_list.append(sum_list[i]+A[i])
#print(sum_list)
modulus = [0 for _ in range(M)]
for i in range(N+1):
    modulus[sum_list[i]%M]+=1
#print(modulus)
cnt = 0
for data in modulus:
    if data>1:
        cnt+=data*(data-1)//2
#print(cnt)

loop = sum(A)
if loop%M == 0:
    cnt-=1

right_list = [0 for i in range(M)]
for i in range(1,N):
    left = (loop - sum_list[i])%M
    cnt+=right_list[(M-left)%M]
    right_list[sum_list[i]%M]+=1
print(cnt)
