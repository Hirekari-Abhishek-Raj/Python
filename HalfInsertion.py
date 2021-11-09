def insertion(lst1):
	for i in range(1,len(lst1)):
		key=lst1[i]
		prev=i-1
		while prev>=0 and key<lst1[prev]:
			lst1[prev+1]=lst1[prev]
			prev=prev-1
		lst1[prev+1]=key
	return lst1
		
string=input("")
lst=[]
for i in string:
	lst.append(i)
length=len(lst)//2
lst=lst[0:length]+insertion(lst[length:])
newstr=""
for i in lst:
	newstr=newstr+i
print(newstr)
