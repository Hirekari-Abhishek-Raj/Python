n=int(input())
lst=[]
for i in range(n):
	lst.append([int(i)for i in input().split()])
lst1=[]
for i in range(len(lst[0])-1,-1,-1):
	temp=[]
	for j in range(len(lst)-1,-1,-1):
		temp.append(lst[j][i])
	lst1.append(temp)
print(len(lst1))
for i in lst1[::-1]:
	for j in i:
		print(j,end=" ")
	print("")
		


