n=int(input())
lst=[int(i)for i in input().split()]
min_count=0
max_count=0
minn=lst[0]
maxx=lst[0]
for i in lst[1:]:
	if i<minn:
		min_count+=1
		minn=i
	elif i>maxx:
		max_count+=1
		maxx=i
# 		print(maxx)
# 		print(max_count)
print(max_count,min_count)
