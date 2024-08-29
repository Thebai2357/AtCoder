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

N = in1()
AC = kn(N)

beans_dict = {}
for i in range(N):
    [taste,color] =AC[i]
    if color in beans_dict:
        if beans_dict[color] > taste:
            beans_dict[color] = taste
        else:
            continue
    else:
        beans_dict[color] = taste
print(max(list(beans_dict.values())))