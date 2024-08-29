def ii():  # 数値受け取り 複数対応
    S = input()
    return map(int,S.split()) if " " in S else int(S)
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(map(int,input().split())) for _ in range(N)] if N!= 0 else list(map(int,input().split()))
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

#N = ii()
# print(str(N)[0],str(N)[1])
# if str(N)[0] == 1 and str(N)[1]!=0:
#     mode = 2
# else:
#     mode = 1
# if mode == 1:
#     if str(N)[0] == 1:
#         top = 9
#     else:
#         top = int(str(N)[0])-1

def mode1(n):
    if n<=10:
        return str(n-1)
    length = len(str(n))-1
    print(length)
    if str(n)[0] == 1:
        top = 9
        length-=1
    else:
        top = int(str(n)[0])-1
    return str(top)+mode1(n-2*pow(10,length)+2*pow(10,length-1))
print(mode1(9))
print(mode1(200))
sum = 1
for i in range(10):
    sum=sum*(10-i)
print(sum)