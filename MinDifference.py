def pair(lst,i,j,n):
    if i==n or j==n:
        return
    if i!=j:
        new.append(abs(lst[i]-lst[j]))
    pair(lst,i+1,j,n)
    pair(lst,i,j+1,n)
    return
n=int(input())
lst=[int(i)for i in input().split()]
new=[]
pair(lst,0,0,n)
print(min(new))
