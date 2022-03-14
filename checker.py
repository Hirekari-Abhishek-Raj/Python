def search(x,lst,start,end): #0,
    if start<=end:
        
        mid=(start+end)//2
        if lst[mid]==x:
            return mid
        if lst[mid]>x:
            return search(x,lst,mid+1,end)
        if lst[mid]<x:
            return search(x,lst,start,mid-1)
    else:
        return -1
    
t=int(input())
for i in range(t):
    lst=[int(i)for i in input().split()]
    n=int(input())
    lst1=[int(i)for i in input().split()]
    for i in lst1:
        print(search(i,lst,0,len(lst)-1))
