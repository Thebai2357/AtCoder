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

def dist(a,b):
    return pow((a[0]-b[0]),2)+pow((a[1]-b[1]),2)

N = in1()
XY = kn(N)
for i in range(N):
    max = 0
    max_node = -1
    for j in range(N):
        if i == j:
            continue
        temp = dist(XY[i],XY[j])
        if temp>max:
            max = temp
            max_node = j+1
    print(max_node)

