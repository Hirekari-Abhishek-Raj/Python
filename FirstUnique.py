for i in range(int(input())):
	string=input("")
	flag=0
	for i in string:
		cnt=string.count(i)
		if cnt==1:
			print(string.index(i))
			flag=1
			break
	if flag==0:
		print(-1)
