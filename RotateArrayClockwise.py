lst=[int(i)for i in input().split()]
m=int(input())
m=m%len(lst)
for i in range(m,len(lst)):
    print(lst[i])
for i in range(m):
    print(lst[i])
