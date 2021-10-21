# your code goes here
n=int(input())
ele=int(input())
sum=0
for i in range(1,n):
    x=int(input())
    if x<ele:
        ele=x
ele=str(ele)
for i in ele:
    sum=sum+int(i)
if sum%2==0:
    print(1)
else:
    print(0)
