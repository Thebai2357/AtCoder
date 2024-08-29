def ii():  # 数値受け取り 複数対応
    S = input()
    return map(int,S.split()) if " " in S else int(S)
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(map(int,input().split())) for _ in range(N)] if N!= 0 else list(map(int,input().split()))
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")
import sys
sys.setrecursionlimit(1000000)
N = ii()
dec = {}
dist_list = {}
for i in range(N-1):
    A,B,C = ii()
    if A not in dec:
        dec[A] = [B]
    else:
        dec[A].append(B)
    if B not in dec:
        dec[B] = [A]
    else:
        dec[B].append(A)
    dist_list[(A,B)] = C
    dist_list[(B,A)] = C
seen = set()
start = 0
for data in dec.keys():
    if len(dec[data]) == 1:
        start = data
        break
def dfs(st,seen):
    search_list = dec[st]
    data_list = []
    for node in search_list:
        if node in seen:
            continue
        temp = seen.copy()
        temp.add(node)
        dfs(node,temp)