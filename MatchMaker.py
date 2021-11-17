for i in range(int(input())):
    n=int(input())
    boys=[int(i)for i in input().split()]
    girls=[int(i)for i in input().split()]
    girls=sorted(girls)
    boys=sorted(boys)
    newb=[]
    for i in range(n-1,-1,-1):
        newb.append(boys[i])
    count=0
    for i in range(n):
        if newb[i]%girls[i]==0 or girls[i]%newb[i]==0:
            count+=1
    print(count)
