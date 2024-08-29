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

N,M=inn()
A=k1()
done = [0 for i in range(M)]
for loop in range(N):
    data = list(inn())
    for gred in range(M):
        done[gred]+=data[gred]
for i in range(M):
    if A[i]>done[i]:
        yn(0)
        exit()
yn(1)
