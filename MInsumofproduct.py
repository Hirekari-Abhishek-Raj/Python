n=int(input())
A=[int(i)for i in input().split()]
B=[int(i)for i in input().split()]
A.sort()
B.sort()
j=n-1
sum=0
for i in range(n):
	sum+=A[i]*B[j]
	j=j-1
print(sum)
