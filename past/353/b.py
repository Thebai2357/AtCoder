N,K = map(int,input().split())
A = list(map(int,input().split()))
rem = K
count = 0
for i in range(N):
    if rem>=A[i]:
        rem -= A[i]
    else:
        count+=1
        rem = K-A[i]
print(count+1)
