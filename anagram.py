t=int(input())
for _ in range(t):
    s,t=input().split()
    dict={}
    flag=0
    for i in s:
    	if i in dict:
    		dict[i]+=1
    	else:
    		dict[i]=1
    x=set()
    for i in t:
        x.add(i)
    # print(x)
    for i in x:
        if i not in dict:
            print(False)
            flag=1
            break
        elif t.count(i)!=dict[i]:
            print(False)
            flag=1
            break
    if flag==0:
        print(True)
