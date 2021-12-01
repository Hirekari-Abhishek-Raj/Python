dic={}
lst=[]
for i in range(int(input())):
	name,sport=input().split()
	if name not in lst:
		lst.append(name)
		if sport not in dic:
			dic[sport]=1
		else:
			dic[sport]+=1
max=float('-inf')
spt=''
for i in dic.keys():
    if dic[i]>max:
        max=dic[i]
        spt=i
print(spt)
if 'football' in dic:
	print(dic['football'])
else:
	print(0)
