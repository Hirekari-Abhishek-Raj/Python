n=int(input())
lst=[]
for i in range(n):
    lst.append(int(input()))
N=int(input())
for i in range(N):
    new=[]
    x=len(lst)
    start=0
    end=x-1
    z=0
    if x%2!=0:
        z=x//2 +1
    else:
        z=x//2
    
    for j in range(z):
        if start!=end:
            y=lst[start]+lst[end]
            new.append(y)
        elif start==end:
            new.append(lst[start])
        start+=1
        end-=1
    lst=new
print(len(lst))
for i in lst:
    print(i)
