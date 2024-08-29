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

N,T=inn()
A=k1()

check_tate_list=[0 for i in range(N)]
check_yoko_list=[0 for i in range(N)]
check_naname_list=[0,0]
def declear(num):
    yoko=(num-1)%N
    tate=(num-1)//N
    if check_tate_list[yoko]==N-1:
        return 1
    else:
        check_tate_list[yoko]+=1

    if check_yoko_list[tate]==N-1:
        return 1
    else:
        check_yoko_list[tate]+=1
    
    if yoko==tate:
        if check_naname_list[0]==N-1:
            return 1
        else:
            check_naname_list[0]+=1
    if yoko+tate==N-1:
        if check_naname_list[1]==N-1:
            return 1
        else:
            check_naname_list[1]+=1
    return 0
for i in range(T):
    if declear(A[i])==1:
        print(i+1)
        exit()
print(-1)