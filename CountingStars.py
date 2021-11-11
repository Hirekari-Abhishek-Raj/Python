for i in range(int(input())):
	n=int(input())
	dict={}
	sum=0
	str=input("")
	for i in str:
		if i not in dict:
			dict[i]=0
			sum=sum+dict[i]
		else:
			dict[i]+=1
			sum=sum+dict[i]
	print(sum)
