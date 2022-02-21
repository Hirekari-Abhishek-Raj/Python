# your code goes here
t=int(input())
for i in range(t):
	n,d=map(int,input().split())
	lst=[int(i)for i in input().split()]
	if d>n:
		d=d%n
	for i in range(d,n):
		print(lst[i],end=" ")
	for i in range(d):
		print(lst[i],end=" ")
