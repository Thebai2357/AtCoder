def i():
    return int(input())
def ii():  # 数値受け取り 複数対応
    return map(int,input().split())
def ai(N = 1):  # 配列受け取り 複数列対応
    return [list(ii()) for _ in range(N)] if N!= 1 else list(ii())
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

def check_rot(n):
    n_list = list(str(n))
    rev = n_list.copy()
    rev.reverse()
    if n%10==0:
        return 0
    for i in range(len(n_list)):
        if n_list[i] != rev[i]:
            return 0
    return 1


import math
N = i()
leg = int(math.pow(N,1/3))
for i in range(leg+1):
    temp = leg-i
    temp = pow(temp,3)
    if check_rot(temp):
        print(temp)
        exit()