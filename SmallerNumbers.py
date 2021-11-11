nums=[]
new=[]
n=int(input())
for i in range(n):
	nums.append(int(input()))
for i in range(n):
	count=0
	for j in range(n):
		if i!=j and nums[i]>nums[j]:
			count+=1
	new.append(count)
for i in new:
	print(i)
