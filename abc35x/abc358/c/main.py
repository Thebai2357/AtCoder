def i():
    return int(input())
def ii():  # 数値受け取り 複数対応
    return map(int,input().split())
def ai(N = 0):  # 配列受け取り 複数列対応
    return [list(ii()) for _ in range(N)] if N!= 0 else list(ii())
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")
def bit_count(self):
    return bin(self).count("1")
N,M = ii()
S = []
# for i in range(N):
#     buy = []
#     data = input()
#     for i in range(M):
#         if data[i] == 'o':
#             buy.append(i)
#     S.append(buy)
# min = N+1
# for i in range(pow(2,N)):
#     current_pop = set()
#     binary = str(bin(i)[2:])
#     binary = list((N-len(binary))*'0'+binary)
#     for j in range(len(binary)):
#         if binary[j] == '1':
#             temp = S[j]
#             for data in temp:
#                 current_pop.add(data)
#     if len(list(current_pop)) == M and bit_count(i) <min:
#         min = bit_count(i)
# print(min)
def bit_count(self):
    return bin(self).count("1")
S = []
for i in range(N):
    data = input().replace('o','1').replace('x','0')
    data = int(data,2)
    S.append(data)
min = N+1
for i in range(pow(2,N)):
    current=0
    for j in range(N):
        if (i>>j)&1:
            current = current | S[j]
    if current == pow(2,M)-1 and bit_count(i) < min:
        min = bit_count(i)
print(min)


