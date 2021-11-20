def find(lst,a,b,c):
    if lst[b]+lst[c]>lst[a] and lst[a]+lst[b]>lst[c] and lst[a]+lst[c]>lst[b]:
        top.append(lst[a]+lst[b]+lst[c])
        return
    if c>0:
        find(lst,a-1,b-1,c-1)
        find(lst,a,b-1,c-1)
        find(lst,a,b,c-1)
    return
    
for i in range(int(input())):
    lst=[int(i)for i in input().split()]
    lst.sort()
    n=len(lst)
    top=[0]
    if n>=3:
        find(lst,n-1,n-2,n-3)
    print(max(top))
	
