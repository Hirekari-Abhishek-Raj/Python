n=int(input())
lst=[int(i)for i in input().split()]
lst1=[]
sum=0
for i in lst:
	if i not in lst1:
		sum=sum+(lst.count(i)//2)
		lst1.append(i)
print(sum)
