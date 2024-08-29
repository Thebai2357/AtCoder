a = list(map(int,input().split()))
b = list(map(int,input().split()))
a_sum = 0
b_sum = 0
for i in range(9):
    a_sum = a_sum+a[i]
    if i!=8:
        b_sum = b_sum+b[i]
print(a_sum-b_sum+1)