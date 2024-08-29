def i():
    return int(input())
def ii():  # 数値受け取り 複数対応
    return map(int,input().split())
def ai(N = 1):  # 配列受け取り 複数列対応
    return [list(ii()) for _ in range(N)] if N!= 1 else list(ii())
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

S = list(input())
big = 0
small = 0
for moji in S:
    if moji.islower():
        small+=1
    else:
        big+=1
temp = ''.join(S)
if small>=big:
    new_word=temp.lower()
else:
    new_word=temp.upper()
print(new_word)