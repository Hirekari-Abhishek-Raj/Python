def func(n,k):
    if n==1:
        return 1
    return ((func(n-1,k)+k-1)%n)+1
for i in range(int(input())):
    n,k=map(int,input().split())
    print(func(n,k))
