n=int(input())
sum=9
y=9
x=9
if n==1:
    print(9)
else:
    for i in range(1,n):
       y=y*10
       x=x+y
       sum=sum+x
    print(sum)
