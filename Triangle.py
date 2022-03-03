# your code goes here
import math
for i in range(int(input())):
	b,a=map(int,input().split())
	h=float((2*a)/b)
	if int(h)==float(h):
		print(int(h))
	else:
		print(int(h)+1)
	
