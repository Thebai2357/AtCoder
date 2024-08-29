def ii():  # 数値受け取り 複数対応
    S = input()
    return map(int,S.split()) if " " in S else int(S)
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(map(int,input().split())) for _ in range(N)] if N!= 0 else list(map(int,input().split()))
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")
def rev(a):
    return(1-a)

N = ii()
H = ai()
time = H[0]
HW = [[H[0],1]]
time_list = [H[0]+1]
for i in range(1,N):
    height = H[i]
    count = 1
    water = height
    length = len(HW)
    for hw in range(length):
        if HW[length-hw-1][0]<height:
            water+= (height-HW[length-hw-1][0])*HW[length-hw-1][1]
            count+=HW[length-hw-1][1]
            HW.pop(-1)
        else:
            break
    HW.append([height,count])
    time+=water
    time_list.append(time+1)
print(*time_list)




