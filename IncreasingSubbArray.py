n=int(input())
lst=[int(i)for i in input().split()]
l=1
s=1
ml=-1
ms=-1
for i in range(1,n):
	if lst[i]>lst[i-1]:
		l+=1
	else:
		if l>ml:
			ms=s
			ml=l
		s=i+1
		l=1
	if l>ml:
		ms=s
		ml=l
if len(lst)>=2:
	print(ml,ms,ms+ml-1)
elif len(lst)==1:
	print(1,1,1)
