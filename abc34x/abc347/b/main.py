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

S = input()
length = len(S)
count = 0
for i in range(length):
    sublen = i+1
    sublist = []
    for j in range(length - sublen + 1):
        if S[j:j+sublen] not in sublist:
            sublist.append(S[j:j+sublen])
    count+=len(sublist)
print(count)