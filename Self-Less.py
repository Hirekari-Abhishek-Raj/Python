t=int(input())
for i in range(t):
	count=0
	n=int(input())
	lst=[int(i)for i in input().split()]
	if n==1:
		print(1)
	else:
		
		mul=1
		for i in lst:
			if i!=0:
				mul=mul*i
			else:
				count+=1
		if count>1:
			for i in lst:
				print(0,end=" ")
		elif count==1:
			for i in lst:
				if i==0:
					print(mul,end=" ")
				else:
					print(0,end=" ")
		else:
			for i in lst:
				print(mul//i,end=" ")
