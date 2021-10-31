n=int(input())
lst=[]
for i in range(n):
    lst.append(int(input()))
lead=[lst[-1]]
maxnum=lst[-1]
if n>2:
    for i in range(n-2,-1,-1):
        if lst[i]>maxnum:
            lead.append(lst[i])
            maxnum=lst[i]
for i in lead:
    print(i)
