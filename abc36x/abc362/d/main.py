def ii():  # 数値受け取り 複数対応
    S = input()
    return map(int,S.split()) if " " in S else int(S)
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(map(int,input().split())) for _ in range(N)] if N!= 0 else list(map(int,input().split()))
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")
N,M = ii()
A = ai()
connect = [[] for _ in range(N)]
for i in range(M):
    u,v,b = ii()
    u-=1
    v-=1
    connect[u].append((v,b))
    connect[v].append((u,b))
# notseen = set([i for i in range(N)])
# dist = [float('inf') for _ in range(N)]
# dist[0] = A[0]
# min_node = 0
# while notseen:
#     connect_list = connect[min_node]
#     length = len(connect_list)
#     for node in range(length):
#         new_node = connect_list[node][0]
#         if new_node in notseen:
#             weight = connect_list[node][1]
#             temp_dist = dist[min_node]+weight+A[new_node]
#             if temp_dist<dist[new_node]:
#                 dist[new_node] = temp_dist
#         else:
#             continue
#     notseen.remove(min_node)
#     new_min = -1
#     new_min_dist = float('inf')
#     for node in notseen:
#         if dist[node]<new_min_dist:
#             new_min = node
#             new_min_dist = dist[node]
#     if new_min == -1:
#         break
#     min_node = new_min

# dist.pop(0)
# print(*dist)
INF = 10**18
from heapq import heappush,heappop
dist_list = [INF for _ in range(N)]
dist_list[0] = A[0]
minHeap = []
connect_list = connect[0]
for new_node,weight in connect_list:
    dist_list[new_node] = A[0]+weight+A[new_node]
    heappush(minHeap,(A[0]+weight+A[new_node],new_node))
while minHeap:
    weight, min_node = heappop(minHeap)
    if weight>dist_list[min_node]:
        continue
    for new_node,weight in connect[min_node]:
        temp_dist = dist_list[min_node]+weight+A[new_node]
        if temp_dist<dist_list[new_node]:
            dist_list[new_node] = temp_dist
            heappush(minHeap,(temp_dist,new_node))
print(*dist_list[1:])



