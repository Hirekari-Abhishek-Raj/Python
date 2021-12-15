def find(lst,l,r,k):
    if l<=r:
        m=(l+r)//2
        if lst[m]==k:
            return m
        if l==r:
            return l
        if lst[m]<k:
            return find(lst,m+1,r,k)
        if k<lst[m]:
            return find(lst,l,m-1,k)
    else:
        return ((l+r)//2)+1
for i in range(int(input())):
    lst=[int(i)for i in input().split()]
    n=int(input())
    lst1=[int(i)for i in input().split()]
    for i in lst1:
        x=(find(lst,0,len(lst)-1,i))
        if lst[x]<i:
            print(x+1)
        else:
            print(x)
