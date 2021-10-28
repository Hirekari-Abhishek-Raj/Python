
n=int(input())
lst=[]
sum=0
k=n-1
for i in range(n):
    lst.append([int(j) for j in input().split()])
for i in range(n):
    sum=sum+lst[i][i]+lst[i][k]
    k-=1

print(sum)
