count=0
for i in range(int(input())):
	string=input("")
	sum=0
	mul=1

	for i in string:
		i=int(i)
		sum=sum+i
		mul=mul*i
	if sum>=mul:
		count+=1
print(count)
