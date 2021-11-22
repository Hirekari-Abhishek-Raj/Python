t=int(input())
print(t)
for i in range(t):
    lst=[int(i)for i in input().split()]
    lst.sort(reverse=True)
    target=sum(lst)//2
    summ=0
    res=[]
    for j in lst:
        summ+=j
        if summ<=target:
            res.append(j)
        else:
            break
    res.sort()
    print(*res)
