def i():
    return int(input())
def ii():  # 数値受け取り 複数対応
    return map(int,input().split())
def ai(N = 1):  # 配列受け取り 複数列対応
    return [list(ii()) for _ in range(N)] if N!= 1 else list(ii())
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")
mod = 998244353
N=i()
import sys

sys.setrecursionlimit(1000000)
def long(n):
    result = 0
    for i in range(n):
        result = (result*pow(10,len(str(n)))+n)%mod
    return result

length = len(str(N))
i=0
def connect(n):
    global i
    if n == 1:
        i = length
        return N%mod
    temp = connect(n//2)
    if n%2 == 0:
        temp = temp*(pow(10,i,mod)+1)%mod
        i=i*2
    else:
        temp = (temp*(pow(10,i,mod)+1)*pow(10,length,mod)+N)%mod
        i=i*2+length
    return temp
print(connect(N))