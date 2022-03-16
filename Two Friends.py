n=int(input())
lstn=[int(i)for i in input().split()]
m=int(input())
lstm=[int(i)for i in input().split()]
new_lst=set()
lst=[]
for i in lstn:
	if i not in lstm:
		new_lst.add(i)
for i in lstm:
	if i not in lstn:
		new_lst.add(i)
for i in new_lst:
    lst.append(i)
lst.sort()
for i in lst:
	print(i)
