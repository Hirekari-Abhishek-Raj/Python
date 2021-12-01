def func(i):
	if i<=9:
		return i
	if i%2==0:
		return func(i-10)
	else:
		return func(i-9)
for i in range(int(input())):
	x=int(input())
	print(func(x))
