n=int(input())
count=1
lst=[int(i)for i in input().split()]
if n==1:
    print(1)
else:
    for i in range(n-1):  #1 2 3 4 5 1 2 3 4 1 2 1 2
        if lst[i]>lst[i+1]:
            count+=1
    print(count)
    
