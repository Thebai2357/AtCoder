def ii():  # 数値受け取り 複数対応
    S = input()
    return map(int,S.split()) if " " in S else int(S)
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(map(int,input().split())) for _ in range(N)] if N!= 0 else list(map(int,input().split()))
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")
import sys
sys.setrecursionlimit(10**6)
N,K = ii()

AB = [list(map(int,input().split())) for _ in range(N-1)]
V = ai()
init = V[0]
V = set(V)
count = 0
if N == 1:
    print(1)
    exit()
def dfs(init,par):
    next_layer = edge_list[init]
    
    contain_flag = 0
    if init in V:
        contain_flag = 1
    for data in next_layer:
        if par == data:
            continue
        result = dfs(data,init)
        if result == 1:
            contain_flag = 1
    global count
    count+=contain_flag
    return contain_flag
edge_list = {}
for i in range(N-1):
    if AB[i][0] not in edge_list:
        edge_list[AB[i][0]] = [AB[i][1]]
    else:
        edge_list[AB[i][0]].append(AB[i][1])
    if AB[i][1] not in edge_list:
        edge_list[AB[i][1]] = [AB[i][0]]
    else:
        edge_list[AB[i][1]].append(AB[i][0])

dfs(init,-1)
print(count)





