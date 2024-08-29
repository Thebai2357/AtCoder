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

N,A,B=inn()
week = A+B
def modulo(str):
    return int(str)%week
D = list(set(list(map(modulo,input().split()))))
D.sort()
for index in range(len(D)-1):
    if D[index+1]-D[index]>=B+1:
        yn(1)
        exit()
if week-(D[-1]-D[0]+1)>=B:
    yn(1)
else:
    yn(0)

