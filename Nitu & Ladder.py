n=int(input())
x=""
for i in range(n-1):
    x=x+" "
y="#"
i=1
while i<=n:
	print(x+y)
	x=x[:len(x)-1]
	y=y+"#"
	i+=1
