def abc(n,count):
    if n==0:
        if count>0:
            cnt.append(count)
            return cnt
        else:
            return 0
    if n==1:
        if count==0:
            cnt.append(1)
            return cnt
        else:
            cnt.append(count)
            return cnt
    abc(n-1,count+1)
    abc(n-2,count+1)
    return cnt
    
    
    
N=int(input())
for i in range(N):
    n=int(input())
    cnt=[]
    x=abc(n,0)
    print(len(x))
