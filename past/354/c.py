N = int(input())
A =[[]for i in range(N)]
for i in range(N):
    a = list(map(int,input().split()))
    a.append(i)
    A[i] = a
A.sort(reverse=True)
print(A)
min= A[0][1]
rem_list = [A[0][2]+1]
for i in range(1,N):
    if A[i][1]<min:
        min = A[i][1]
        rem_list.append(A[i][2]+1)
rem_list.sort()
print(rem_list)
print(*rem_list)