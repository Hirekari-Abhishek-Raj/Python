def abc(i,total,count):
    if i==n and total==target:
        count+=1
        return count
    abc(i+1,total+lst[i],count)
    abc(i+1,total-lst[i],count)
    abc(i+1,total,count)
    return count
target=int(input())
n=int(input())
lst=[int(i)for i in input().split()]
print(abc(0,0,0))
