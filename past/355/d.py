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

N=in1()
lr_list=kn(N)
lr_list.sort()
rem=[]
temp=[0,0]
count=0
length=0
for loop in range(N):
    temp=lr_list.pop(0)
    while(rem):
        if rem[0]<temp[0]:
            rem.pop(0)
        else:
            break
    count+=len(rem)
    rem.append(temp[1])
    rem.sort()
print(count)