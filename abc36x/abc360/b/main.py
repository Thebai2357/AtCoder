def ii():  # 数値受け取り 複数対応
    S = input()
    return map(int,S.split()) if " " in S else int(S)
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(map(int,input().split())) for _ in range(N)] if N!= 0 else list(map(int,input().split()))
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")

S,T = input().split()
if len(T)==1:
    for i in range(len(S)-1):
        if S[i] == T:
            print('Yes')
            exit()
else:
    for i in range(len(S)-1):
        if T[0] == S[i]:
            for w in range(max(1,i),len(S)-i):
                if i+w>=len(S):
                    break
                if S[i+w] != T[1]:
                    continue
                result = ''
                for res in range(len(S)):
                    if res%w == i:
                        result+=S[res]
                if result == T:
                    print('Yes')
                    exit()
print('No')
