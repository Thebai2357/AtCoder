def i():
    return int(input())
def ii():  # 数値受け取り 複数対応
    return map(int,input().split())
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(ii()) for _ in range(N)] if N!= 0 else list(ii())
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

S= input()
count = [0 for _ in range(26)]
for word in S:
    count[ord(word)-97]+=1
for i in range(26):
    if count[i] == max(count):
        print(chr(97+i))
        exit()