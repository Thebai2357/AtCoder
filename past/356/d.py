def in1():
    return int(input())
def inn():
    return map(int,input().split())
def k1():
    return list(inn())
def kn(N):  # A[N][k]でアクセス
    return [k1() for _ in range(N)]
def YN(BOOL):   # 大文字YES NO
    print("YES" if BOOL==1 else "NO")
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")
def fj():
    return in1(),k1()
mod = 998244353


def myfunc(digit):
    temp = (N+1)//pow(2,digit+1)
    rem = (N+1)%pow(2,digit+1)
    return (temp*pow(2,digit)+max(0,rem-pow(2,digit)))%mod

N,M=inn()
m=str(bin(M))
mstrlist = list(m[2:][::-1])
mlist = [int(i) for i in mstrlist]
sum = 0
for i in range(len(mlist)):
    if mlist[i] == 1:
        temp = myfunc(i)
        sum = (sum + temp)%mod
print(sum)
