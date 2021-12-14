# 4 5 6 7 0 1 2 3
n=int(input())
lst=[int(i)for i in input().split()]
if n==1:
    print(lst[0])
elif n==2:
    print(min(lst))
else:
    for i in range(1,n):
        if lst[n-i]<lst[n-i-1]:
            a=lst[n-i]
            break
        if lst[i]<lst[i-1]:
            a=lst[i]
            break
    print(a)
        
