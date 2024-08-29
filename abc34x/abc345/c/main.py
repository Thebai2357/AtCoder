def ii():  # 数値受け取り 複数対応
    S = input()
    return map(int,S.split())
def ai(N = 1):  # 配列受け取り 複数列対応
    return [list(ii()) for _ in range(N)] if N!= 1 else list(ii())
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

S = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'
alist = [0 for i in range(26)]
for al in S:
    for i in range(26):
        if al == alpha[i]:
            alist[i] += 1
            break

sum = len(S)*(len(S)-1)
flag = 0
for data in alist:
    if data == 0 or data == 1:
        continue
    else:
        sum -= data*(data-1)
        flag = 1
sum = sum//2 +flag
print(sum)
