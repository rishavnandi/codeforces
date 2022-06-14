l1=[]
for _ in range(int(input())):
    l=[]
    input()
    input_list = list(map(int, input().split()))
    for i in input_list:
        if i not in l:
            l.append(i)
    if (len(input_list) - len(l))%2!=0:
        l.pop(0)
    l1.append(len(l))
for i in l1:
    print(i,end='\n')