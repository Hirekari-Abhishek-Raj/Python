# your code goes here
n=int(input())
lst=[int(i)for i in input().split()]
lst.sort()
m=lst[1]-lst[0]
for i in range(1,n):
    m=min(m,(lst[i]-lst[i-1]))
print(m)
