def insertionsort(lst):
    for i in range(1,n+1):
        key=lst[i]
        prev=i-1
        while prev>=0 and lst[prev]>key:
            lst[prev+1]=lst[prev]
            prev=prev-1
        lst[prev+1]=key
    return lst
n,k=map(int,input().split())
lst=[int(i)for i in input().split()]
lst.append(k)
print(insertionsort(lst))
