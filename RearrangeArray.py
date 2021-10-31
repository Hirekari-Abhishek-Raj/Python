n=int(input())
num=[]
ind=[]
for i in range(n):
    num.append(int(input()))
for i in range(n):
    ind.append(int(input()))
target=[num[0]]
for i in range(1,n):
    target=target[:ind[i]]+[num[i]]+target[ind[i]:]
for i in target:
	print(i)
