N = int(input())
a = pow(10,8)
def myfunc(i):
    return int(i)%a
A = list(map(myfunc,input().split()))
A.sort()
sum = 0
count = 0
ptr = N-1
for i in range(N):
    sum+=A[i]
    temp = a-A[i]
    while True:
        if ptr==0:
            count+=N
            break
        if A[ptr]>temp:
            ptr = ptr-1
        else:
            count+=(N-ptr-1)
            break
count=count//2
sum = sum*(N-1)-a*count
print(sum)

N = int(input())
A = list(map(int,input().split()))
sum = 0
a = pow(10,8)
for i in range(N-1):
    for j in range(i+1,N):
        sum+=((A[i]%a+A[j]%a)%a)
print(sum)