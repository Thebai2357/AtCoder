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

S = list(input())
S.sort()
#print(S)
count_list = []
while S:
    temp = S.pop(0)
    count = 1
    while S:
        if S[0] == temp:
            count+=1
            S.pop(0)
        else:
            break
    count_list.append(count)
#    print(count_list)
count_list.sort()
while True:
    if len(count_list) == 0:
        yn(1)
        break
    elif len(count_list)== 1:
        yn(0)
        break
    elif (count_list[0]==count_list[1]) and (len(count_list)==2 or (count_list[1]!= count_list[2])):
        del count_list[:2]
    else:
        yn(0)
        break

