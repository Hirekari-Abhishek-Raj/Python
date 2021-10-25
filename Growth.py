
n=int(input())
sum=0
for i in range(n):
    sum=sum+int(input())
if sum/n>100:
    print("Excellent!")
else:
    print("Not Excellent!")
