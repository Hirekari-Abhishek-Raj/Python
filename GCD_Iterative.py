def gcd(y,z):
    lst=[]
    res=0
    for i in range(1,z+1):
        if z%i==0:
            lst.append(i)
    for i in range(len(lst)-1,-1,-1):
        if y%lst[i]==0:
            res=lst[i]
            break
    return res
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if a==b:
        print(a)
    else:
        if a>b:
            x=gcd(a,b)
            print(x)
        else:
            x=gcd(b,a)
            print(x)
