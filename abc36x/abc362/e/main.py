def ii():  # 数値受け取り 複数対応
    S = input()
    return map(int,S.split()) if " " in S else int(S)
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(map(int,input().split())) for _ in range(N)] if N!= 0 else list(map(int,input().split()))
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")
mod = 998244353
N = ii()
A = ai()
# sum = [0 for _ in range(N)]
# arr = []
# for i in range(N):
#     if len(arr) <= 1:
#         arr.append(A[i])
#     elif len(arr) > 1:
#         now = A[i]
#         if arr[0]-arr[1] == arr[-1]-now:
#             arr.append(now)
#         else:
#             length = len(arr)
#             for i in range(length):
#                 sum[i] = (sum[i]+length-i)%mod
#             arr = [arr[-1],now]
# length = len(arr)
# for i in range(length):
#     sum[i] = (sum[i]+length-i)%mod
# print(*sum)
A.sort()
uset = set(A)
unique = list(set(A))
hist = []
for data in unique:
    hist.append(A.count(data))
unique.sort()
count = len(unique)
sum = 
for st in range(count):
    for step in range(1,count-st):
        equal = [unique[st],unique[st+step]]
        diff = unique[st+step]-unique[st]
        i = 0
        while True:
            if unique[st]+(i+2)*diff in uset:
                equal.append(unique[st]+(i+2)*diff)
                i+=1
            else:
                break
        





