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
B=k1()
A.sort()
B.sort()
a_flag=0
for i in range(N+M):
    if not A:
        B.pop(0)
        a_flag=0
    elif not B:
        A.pop(0)
        a_flag+=1
    else:
        if A[0]<B[0]:
            A.pop(0)
            a_flag+=1
        else:
            B.pop(0)
            a_flag=0
    if a_flag==2:
        yn(1)
        exit()
yn(0)