def abc(n):    
    if n==1:
        return 1
    if n<=0:
        return 0
    x=0
    y=0
    if n%20==0:
        x= abc(n//20) 
    if n%10==0:
        y= abc(n//10)
    if x==1 or y==1:
        return 1
    else:
        return 0
    
    
N=int(input())
for i in range(N):
    n=int(input())
    if abc(n)==1:
        print("Yes")
    else :
        print("No")
