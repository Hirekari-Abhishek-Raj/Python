# your code goes here
N=int(input())
lst=[int(i)for i in input().split()]
s=set()
for i in lst:
	s.add(i)
if len(s)>N//2:
	print(N//2)
else:
	print(len(s))
