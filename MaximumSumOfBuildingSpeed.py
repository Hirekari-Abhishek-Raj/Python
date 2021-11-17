n=int(input())
lst=[int(i) for i in input().split()]
lst.sort()
sum=0
for i in range(0,(2*n)-1,2):
    min_value=min(lst[i],lst[i+1])
    sum+=min_value
print(sum)
