t = int(input())
l=[]
for i in range(t):
    x=0
    a,b,c,d = map(int, input().split())
    if b>a:
        x+=1
    if c>a:
        x+=1
    if d>a:
        x+=1
    l.append(x)
for i in l:
    print(i,end='\n')