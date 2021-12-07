for i in range(int(input())):
	s=float(input())
	if s<=100:
		if s<38:
			print(int(s))
		else:
			if s%5==0:
				print(int(s))
			elif s%5>=3:
				print(int((s-(s%5))+5))
			else:
				print(int(s))
