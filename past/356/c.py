def in1():
    return int(input())
def inn():
    return map(int,input().split())
def k1():
    return list(inn())
def kn(N):  # A[N][k]でアクセス
    return [k1() for _ in range(N)]
def YN(BOOL):   # 大文字YES NO
    print("YES" if BOOL==1 else "NO")
def yn(BOOL):   # 小文字Yes No
    print("Yes" if BOOL==1 else "No")
def fj():
    return in1(),k1()
N,M,K=inn()

def test(data_res,assume):
    data,result = data_res[0],data_res[1]
    temp = data&assume
    count = temp.bit_count()
    if (count>=K and result == 'o') or (count<K and result == 'x'):
        return True
    else:
        return False


data_res_list = []

for loop in range(M):
    data = list(input().split())
    count = int(data.pop(0))
    result = data.pop(-1)
    data = [int(i) for i in data]
    temp = 0
    for i in range(count):
        temp+=pow(2,N-data[i])
    data_res_list.append([temp,result])
count = 0
for i in range(pow(2,N)):
    flag = 0
    for data_res in data_res_list:
        if test(data_res,i) == False:
            flag = 1
            break
    if flag == 0:
        count+=1
print(count)