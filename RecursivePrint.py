def abc(first,last):
    if first==last:
        lst.append(last)
        return lst
    lst.append(first)
    abc(first+1,last)
    return lst
N=int(input())
for i in range(N):
    first,last=map(int,input().split())
    lst=[]
    print(" ".join(str(i)for i in abc(first,last)))
