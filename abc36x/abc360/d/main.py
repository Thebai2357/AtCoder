def ii():  # 数値受け取り 複数対応
    S = input()
    return map(int,S.split()) if " " in S else int(S)
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(map(int,input().split())) for _ in range(N)] if N!= 0 else list(map(int,input().split()))
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")
from collections import deque
que = deque()

N,T = ii()
S = list(input())
X = ai()
xs = []
for i in range(N):
    xs.append([X[i],S[i]])
xs.sort()

num = 0
sum = 0
for i in range(N):
    x = xs[i][0]
    s = xs[i][1]
    if s == '1':
        que.append(x+2*T+0.1)
        num+=1
    else:
        while que: 
            if que[0]<x:
                _ = que.popleft()
                num -=1
            else:
                break
        sum+=num
    #print(que)
print(sum)