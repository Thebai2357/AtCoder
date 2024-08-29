def ii():  # 数値受け取り 複数対応
    S = input()
    return map(int,S.split()) if " " in S else int(S)
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(map(int,input().split())) for _ in range(N)] if N!= 0 else list(map(int,input().split()))
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

N = ii()
A = ai()
B = A.copy()
B.sort()
B.reverse()
sum_list = {}
sum = 0
i = 0
while True:
    if i ==N:
        break
    if B[i] not in sum_list:
        sum_list[B[i]] = sum
    sum+=B[i]
    i+=1
for i in range(N):
    if i != N-1:
        print(sum_list[A[i]],end = ' ')
    else:
        print(sum_list[A[i]])




