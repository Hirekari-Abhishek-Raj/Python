n=int(input())
flag=0
prev=int(input())
for i in range(1,n):
	pres=int(input())
	if pres+prev>100:
		flag=1
	prev=pres
if flag==1:
	print(True)
else:
	print(False)
