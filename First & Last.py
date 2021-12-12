def find(lst,l,r):
    if l<=r:
        m=(l+r)//2
        if lst[m]==k:
            return m
        if l==r:
            return
        if lst[m]<k:
            return find(lst,m+1,r)
        if k<lst[m]:
            return find(lst,l,m-1)
n=int(input())
lst=[int(i)for i in input().split()]
k=int(input())
l=0
r=n
x=find(lst,l,r)
if x==None:
    print(-1,-1)
else:
    if x==0:
        for i in range(1,n):
            if lst[i]!=k:
                y=i-1
    elif x==n-1:
        #print("hi")
        #print(n)
        for i in range(x-1,-1,-1):
            #print(i)
            if lst[i]!=k:
                y=i+1
                break
        x,y=y,x
    else:
        y=x
        while x>=1 and y<=n-2:
            if lst[x-1]==k:
                x=x-1
            if lst[y+1]==k:
                y=y+1
            #print(x,y)
            if x-1==0 or y+1==n-1:
                break
            if lst[x-1]!=k and lst[y+1]!=k:
                break
        while x>=1:
            if lst[x-1]==k:
                x=x-1
            else:
                break
        while y<=n-2:
            if lst[y+1]==k:
                y=y+1
            else:
                break
    print(x,y)
            
