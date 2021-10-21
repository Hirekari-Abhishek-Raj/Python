n=int(input())
sum=0
for i in range(n):
    if i==0:
        sum=sum+int(input())
    elif i>0 and i%2==0:
        sum=sum-int(input())
    elif i>0 and i%2!=0:
        sum=sum+int(input())
print(sum)
