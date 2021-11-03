def rec(n):                         #n=2
    if n==1:                        
        return 1                        
    else:      
        x=1+((n*(n-1))//2)
        y=x+n
        a=1
        for i in range(x,y):
            a=a*i
        sum=a+rec(n-1)
        return sum                          
N=int(input())                              
for i in range(N):                          
    n=int(input())                              
    print(rec(n))                               
