n=int(input())
lst=input('')
new=''
lower=[]
upper=[]
for i in lst:
	if i.isupper():
		upper.append(i)
	else:
		lower.append(i)
upper.sort()
lower.sort()
ui=0
li=0
for i in lst:
    if i.isupper():
        new=new+upper[ui]
        ui+=1
    else:
        new=new+lower[li]
        li+=1
print(new)
