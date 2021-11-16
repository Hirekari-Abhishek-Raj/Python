n,k=map(int,input().split())
lst=[int(i)for i in input().split()]
charged=int(input())
x=(sum(lst)-lst[k])//2
if x==charged:
	print("It is Correct!")
else:
	print(charged-x)
