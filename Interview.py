F=[]
M=[]
for i in range(int(input())):
	a,b=map(int,input().split())
	if a==0:
		F.append(b)
	else:
		M.append(b)
M.sort(reverse=True)
F.sort(reverse=True)
print(*(F+M))
