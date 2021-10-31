def dec(lst):
	for i in range(1,n):
		if lst[i]>lst[i-1]:
			return False
	return True
def inc(lst):
	for i in range(1,n):
		if lst[i]<lst[i-1]:
			return False
	return True
n=int(input())
lst=[]
res=False
for i in range(n):
	lst.append(int(input()))
if n>2:
	if lst[0]>lst[1]:
		res=dec(lst)
	else:
		res=inc(lst)
print(res)
		
