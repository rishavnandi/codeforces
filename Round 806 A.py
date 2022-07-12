
t = int(input())
l = []
for i in range(t):
    l.append(input())
for i in l:
    if i.lower() == "yes":
        print("YES")
    else:
        print("NO")
