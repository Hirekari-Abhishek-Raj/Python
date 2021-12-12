n=int(input())
lst=[int(i)for i in input().split()]
p,q=map(int,input().split())
x=-1
y=-1
for i in range(n):
    if lst[i]>=p:
        x=i
        break
for j in range(n-1,-1,-1):
    #print(j,lst[j])
    if lst[j]<=q:
        y=j
        break
if x==-1 or y==-1 or x>y:
    print(-1,-1)
else:
    print(x,y)
