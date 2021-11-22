n,k=map(int,input().split())
lst=[]
new=[]

for i in range(n):
    lst.append(input(""))
for i in range(k):
    count=0
    for j in range(1,n):
        if lst[j][i]>lst[j-1][i]:
            continue
        else:
            count+=1
    if count>0:
        new.append(count)
print(len(new))
