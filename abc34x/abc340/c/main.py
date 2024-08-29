def i():
    return int(input())
def ii():  # 数値受け取り 複数対応
    return map(int,input().split())
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(ii()) for _ in range(N)] if N!= 0 else list(ii())
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")
import sys
sys.setrecursionlimit(10**6)
N = i()
sum = 0
num = 0
memo = {}
def myfunc(n):
    if n == 1:
        return 0
    if n in memo.keys():
        return memo[n]
    if n%2 == 0:
        temp = myfunc(n//2)
        paid = temp*2+n
    else:
        low = myfunc(n//2)
        high = myfunc(n//2+1)
        paid = low+high+n
    memo[n] = paid 
    return paid

print(myfunc(N))
