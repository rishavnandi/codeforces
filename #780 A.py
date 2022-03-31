n = int(input())
h = []
a = []
ans = 0
for i in range(n):
	hh, aa = map(int, input().split())
	h.append(hh)
	a.append(aa)
for i in range(len(a)):
    a[i]=a[i]*2
for i in range(len(h)):
    if h[i]==0 and a[i]==0:
        print(1)
    elif h[i]==0 and a[i]!=0:
        print(1)
    else:
        print((h[i]+a[i])+1)