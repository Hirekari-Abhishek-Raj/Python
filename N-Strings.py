n=int(input())
count=0
for i in range(n):
	x=input("")
	if len(x)%2!=0:
		count+=1
print(count)
