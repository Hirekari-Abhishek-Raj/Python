def binary(i,count):
    while i>=0:
        if i==0:
            return count
        if i==1:
            count+=1
            return count
        if i%2==1:
            count+=1
        i=i//2
        
    
    return  count
n=int(input())
lst=[int(j)for j in input().split()]
countlist=[]
for i in lst:
    count=0
    x=binary(i,count)
    countlist.append([i,x])
countlist.sort(key=lambda x:x[1],reverse=True)
for i in countlist:
    print(i[0],end=" ")
