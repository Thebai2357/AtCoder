def i():
    return int(input())
def ii():  # 数値受け取り 複数対応
    return map(int,input().split())
def ai(N = 1):  # 配列受け取り 複数列対応
    return [list(ii()) for _ in range(N)] if N!= 1 else list(ii())
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

after = [chr(97+i) for i in range(26)]
N = i()
S = list(input())
Q = i()
CD = [list(input().split()) for _ in range(Q)]
for cd in CD:
    for j in range(26):
        if after[j] == cd[0]:
            after[j] = cd[1]
for s in range(len(S)):
    S[s] = after[ord(S[s])-97]
print("".join(S))