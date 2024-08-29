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

N,L,R=inn()
data = []
for i in range(1,L):
    data.append(i)
for i in range(L,R+1):
    data.append(L+R-i)
for i in range(R+1,N+1):
    data.append(i)
print(*data)