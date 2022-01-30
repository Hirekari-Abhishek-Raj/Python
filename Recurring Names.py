# your code goes here
k=int(input())
lst=[str(i)for i in input().split()]
dict={}
flag=1
for i in lst:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
lst=sorted(dict,key = lambda x:x)
for i in lst:
	if dict[i]>k:
		print(i)
		flag=0
if flag==1:
	print("no such names in this town!!!")
