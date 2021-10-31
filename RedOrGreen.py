n=str(input())
RC=0
GC=0
for i in n:
	if i=="R":
		RC+=1
	else:
		GC+=1
print(min(RC,GC))
