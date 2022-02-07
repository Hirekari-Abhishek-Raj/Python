# your code goes here
lst=[str(i) for i in input().split(" ")]
max=0
for i in lst:
	if max<len(i):
		max=len(i)
print(max)
