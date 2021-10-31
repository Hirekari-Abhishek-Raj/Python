n=int(input())
lst=[]
for i in range(n):
    x=int(input())
    lst.append(x*x)
lst.sort()
for i in lst:
    print(i)
