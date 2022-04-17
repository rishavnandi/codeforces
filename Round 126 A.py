n = int(input())
for i in range(n):
    x = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    for i in range(1,x):
        if a[i-1]==b[i]:
            a[i],b[i]=b[i],a[i]
    sum_a = 0
    for i in range(1,x):
        sum_a += a[i]-a[i-1]
    sum_b = 0
    for i in range(1,x):
        sum_b += b[i]-b[i-1]
    _sum = sum_a - sum_b
    ans = []
    ans.append(_sum)
for i in ans:
    print(i)
