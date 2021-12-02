for i in range(int(input())):
	n=int(input())
	v=n-1
	res=0
	lst=[int(i)for i in input().split()]
	lst.sort(reverse=True)
	for i in lst:
		res+=i*v
		v=v-2
	print((lst[0]*res)%(1000000007))
