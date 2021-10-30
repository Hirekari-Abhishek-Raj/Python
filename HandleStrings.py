n=int(input())
for i in range(n):
	lst=[]
	x=str(input())
	res="-"
	for i in x:
		lst.append(i)
	if len(lst)%3==0 and len(lst)%5==0:
		res="foobar"
	elif len(lst)%3==0:
		res="foo"
	elif len(lst)%5==0:
		res="bar"
	print(res)
