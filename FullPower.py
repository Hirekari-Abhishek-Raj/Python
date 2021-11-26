t=int(input())
for i in range(t):
    n=int(input())
    lst=[int(i)for i in input().split()]
    mx=max(lst)
    mn=min(lst)
    if n==2:
    	print(mx-mn)
    elif lst[0]==mx and lst[-1]==mn:
    	lst.sort()
    	print(max((lst[-2]-lst[0]),(lst[-1]-lst[1])))
    else:
    	print(mx-mn)
		
