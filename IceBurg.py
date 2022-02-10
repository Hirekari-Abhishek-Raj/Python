# your code goes here
l=int(input())
b=int(input())

if l<1 or b<1:
	print(500)
else:
	radius=abs(l+b)+abs(l-b)+abs(l/b)+abs(l*b)
	print(radius)
